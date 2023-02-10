from django.db import models

class Currency(models.Model):
    last_updated = models.CharField(max_length=20, verbose_name='기준날짜')
    krw2usd = models.CharField(max_length=20, verbose_name='달러')
    jpy2usd = models.CharField(max_length=20, verbose_name='엔화')

    def __str__(self):
        return self.last_updated
