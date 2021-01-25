from django.conf.urls import url

from trade_bot.views import AddCandles

urlpatterns = [
    url(r'candles/add/$', AddCandles.as_view())
]