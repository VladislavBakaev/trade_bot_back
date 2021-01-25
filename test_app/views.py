from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

class TestMetod(APIView):
    def get(self, request):
        print('get metod')
        
        #return JsonResponse({}, status = 200)
        return HttpResponse('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Пример веб-страницы</title></head><body><h1>Заголовок</h1><!-- Комментарий --><p>Первый абзац.</p><p>Второй абзац.</p></body></html>')
    
    def post(self, request):
        print('post metod')

        return JsonResponse({}, status = 200)