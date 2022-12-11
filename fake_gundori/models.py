# django model 관련
from django.db import models
from django.urls import reverse
from django.utils import timezone
from dateutil.relativedelta import relativedelta

ARMY = '육군'
NAVY = '해군'
AIR = '공군'
MARINE = '해병대'
PUBLIC = '공익'
ARMY_CHOICE = ((ARMY, '육군'), (NAVY, '해군'), (AIR, '공군'), (MARINE, '해병대'), (PUBLIC, '공익'))

class Soldier(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
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
        if army_choice == "육군":
            end_date = enter_date + relativedelta(months=18) + relativedelta(days=-1)
        if army_choice == "해군":
            end_date = enter_date + relativedelta(months=20) + relativedelta(days=-1)
        if army_choice == "공군":
            end_date = enter_date + relativedelta(months=21) + relativedelta(days=-1)
        if army_choice == "공익":
            end_date = enter_date + relativedelta(months=21) + relativedelta(days=-1)
        if army_choice == "해병대":
            end_date = enter_date + relativedelta(months=18) + relativedelta(days=-1)
        return end_date

    # 계급
    @property
    def military_rank(self):
        enter_date = self.enter_date
        g2 = (enter_date + relativedelta(months=3)).replace(day=1)
        g3 = (g2 + relativedelta(months=6)).replace(day=1)
        g4 = (g3 + relativedelta(months=6)).replace(day=1)
        now = timezone.now()
        if now < g2:
            military_rank = '이병'
        elif now < g3:
            military_rank = '일병'
        elif now < g4:
            military_rank = '상병'
        else:
            military_rank = '병장'
        return military_rank

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

    # 현재 복무일수
    @property
    def days_until_now(self):
        total_days = self.total_days
        remain_days = self.remain_days
        return total_days - remain_days

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
        return round(percent)