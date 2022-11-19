from django.db import models
from django.utils import timezone

ARMY = 'army'
NAVY = 'navy'
AIR = 'air'
ARMY_CHOICE = ((ARMY, '육군'), (NAVY, '해군'), (AIR, '공군'))

class Soldier(models.Model):
    name = models.CharField(max_length=30)
    enter_date = models.DateTimeField()
    army_choice = models.CharField(choices=ARMY_CHOICE, max_length=30)

    def __str__(self):
        return self.name