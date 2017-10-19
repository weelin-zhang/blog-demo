# encoding:utf8
"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import *
from django.views.generic import TemplateView


app_name = 'comments'
urlpatterns = [
    url(r'^post/(?P<post_pk>\d+)/$', PostCommentView.as_view(), name='post_comment'),
    # url(r'^post/(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    # url(r'date/(?P<year>\d{4})/(?P<month>\d{1,2})/$', ArchDateView.as_view(), name='arch_date'),
    # url(r'category/(?P<category>\w+)/$', ArchCategoryView.as_view(), name='arch_category'),

]
