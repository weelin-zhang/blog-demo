# encoding:utf8
from django.conf.urls import url, include


import testajax
from .views import *

app_name = "testajax"
urlpatterns = [
    url(r'^load', load, name='load'),
    url(r'^backresult/(?P<method>\w+)/$', backresult, name='backresult'),
    url(r'^get/$', get_method, name='get_method'),
    url(r'^post/$', post_method, name='post_method'),
]