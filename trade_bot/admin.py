from django.contrib import admin

from trade_bot.models import Candle, DepthOfMarket

# Register your models here.

@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    list_display = ('date', 'open_price', 'close_price', 'hight_price', 'low_price')