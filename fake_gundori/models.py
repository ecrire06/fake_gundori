from django.db import models
from django.utils import timezone

# 병사
# 이름, 입대일, 병역, 

class Soldier(models.Model):
    name = models.CharField(max_length=30)
    enter_date = models.DateTimeField(default=timezone.now)
    ARMY = 'army'
    NAVY = 'navy'
    AIR = 'air'
    ARMY_CHOICE = ((ARMY, '육군'), (NAVY, '해군'), (AIR, '공군'))
    army_choice = models.CharField(choices=ARMY_CHOICE, max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name