from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
import datetime

from rest_framework.views import APIView
from rest_framework.serializers import Serializer

from trade_bot.models import Candle, DepthOfMarket

class AddCandles(APIView):

    def post(self, request):
        candles = request.data.get('candles')
        print(candles[0])
        candles_list = []
        for candle in candles:
            new_candle = Candle(
                date = datetime.datetime.fromtimestamp(candle.get('date')),
                open_price = candle.get('open'),
                close_price = candle.get('close'),
                hight_price = candle.get('hight'),
                low_price = candle.get('low')
            )
            candles_list.append(new_candle)
        Candle.objects.bulk_create(candles_list)
        return JsonResponse({},status=200)

class AddDepthOfMarket(APIView):

    def post(self, request):
        pass

