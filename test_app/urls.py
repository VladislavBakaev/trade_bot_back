from django.conf.urls import url

from test_app.views import TestMetod

urlpatterns = [
    url(r'test/$', TestMetod.as_view())
]