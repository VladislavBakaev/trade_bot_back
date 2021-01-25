from django.db import models

# Create your models here.

class Candle(models.Model):
    date = models.DateTimeField()
    open_price = models.DecimalField(max_digits=12, decimal_places=8)
    close_price = models.DecimalField(max_digits=12, decimal_places=8)
    hight_price = models.DecimalField(max_digits=12, decimal_places=8)
    low_price = models.DecimalField(max_digits=12, decimal_places=8)

    class Meta:
        db_table = "candles"

class DepthOfMarket(models.Model):

    class Meta:
        db_table = 'depth of market'

