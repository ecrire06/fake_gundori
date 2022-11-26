# django model 관련
from django.db import models
from django.urls import reverse
from django.utils import timezone

# date 관련
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

ARMY = 'army'
NAVY = 'navy'
AIR = 'air'
ARMY_CHOICE = ((ARMY, '육군'), (NAVY, '해군'), (AIR, '공군'))

class Soldier(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default="password")
    enter_date = models.DateTimeField()
    army_choice = models.CharField(choices=ARMY_CHOICE, max_length=30, null=True)
    bio = models.CharField(max_length=200, null=True, blank=True, default="한줄소개")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('soldier_detail', kwargs={'pk': self.pk})

    # 전역일
    @property
    def end_date(self):
        enter_date = self.enter_date
        army_choice = self.army_choice
        if army_choice == "army":
            end_date = enter_date + relativedelta(months=18) + relativedelta(days=-1)
        if army_choice == "navy":
            end_date = enter_date + relativedelta(months=20) + relativedelta(days=-1)
        if army_choice == "air":
            end_date = enter_date + relativedelta(months=21) + relativedelta(days=-1)
        return end_date

    # 남은 복무일수
    @property
    def remain_days(self):
        end_date = self.end_date
        remain_days = (end_date - timezone.now()).days
        if remain_days < 0:
            remain_days = 0
        return remain_days
    
    # 총 복무일수
    @property
    def total_days(self):
        end_date = self.end_date
        enter_date = self.enter_date
        return (end_date - enter_date).days

    # 복무 퍼센트
    @property
    def percent(self):
        end_date = self.end_date
        enter_date = self.enter_date
        serve_timedelta = (timezone.now() - enter_date) # datetime.timedelta object
        total_timedelta = (end_date - enter_date) #datetime.timedelta object
        percent = serve_timedelta.total_seconds() / total_timedelta.total_seconds() * 100
        if percent > 100:
            percent = 100
        if percent < 0:
            percent = 0
        return "{0} %".format(round(percent, 8))