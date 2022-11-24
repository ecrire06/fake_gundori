# django model 관련
from django.db import models
from django.utils import timezone

# date 관련
from datetime import datetime
from dateutil.relativedelta import relativedelta

ARMY = 'army'
NAVY = 'navy'
AIR = 'air'
ARMY_CHOICE = ((ARMY, '육군'), (NAVY, '해군'), (AIR, '공군'))

class Soldier(models.Model):
    name = models.CharField(max_length=30)
    enter_date = models.DateTimeField()
    army_choice = models.CharField(choices=ARMY_CHOICE, max_length=30, null=True)

    def __str__(self):
        return self.name

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
        return remain_days    
    
    # 복무 퍼센트