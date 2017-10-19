# encoding:utf8
import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
from django.core import serializers
# Create your views here.


def backresult(request, method, *args, **kwargs):
    if method == 'load':
        return HttpResponse(request.GET.get('data', 'default'))
    elif method =='get':
        d_l = {"data_l": [{"name": 'zwj', 'age': 1},
                          {"name": 'weelin1', 'age': 200},
                          {"name": 'weelin2', 'age': 250},
                          {"name": 'weelin3', 'age': 300},
                          {"name": 'weelin4', 'age': 400},
                          ],
               'msg': "ok",
               }

        return HttpResponse(json.dumps(d_l))


def load(request, *args, **kwargs):
    return HttpResponse('ok')
    return render(request, 'testajax/load.html')


def get_method(request, *args, **kwargs):

    return render(request, 'testajax/get_method.html', {'data_l': [
        {'name': 'a', 'age': 9},
        {'name': 'b', 'age': 10},
    ]})


def post_method(request, *args, **kwargs):
    sort = request.POST.get('sort', request.GET.get('sort', 'up'))
    current_index = int(request.POST.get('pageIndex', 1))
    all_infos = UserInfo.objects.all()
    if sort == 'down':
        all_infos = UserInfo.objects.all().order_by('-name')
    all_count = len(all_infos)
    num_per_page = 10
    page_nums = (all_infos.count()+num_per_page-1)//num_per_page
    # print(page_nums)
    start_index = (current_index-1)*num_per_page
    end_index = current_index*num_per_page-1
    page_infos = all_infos[start_index:end_index]
    if request.method != 'POST':
        return render(request, 'testajax/post_method.html', {'data_l': page_infos, 'all_count':all_count, 'pages': page_nums, 'sort': sort})
    elif request.POST.get('name') == 'zwj':
        return HttpResponse(json.dumps({'data_l': [{'name': 'zzz', 'age': 1000}]}), content_type='json')
    else:
        print(sort)
        page_infos = serializers.serialize('json', page_infos)  #里面也进行了序列化，后端需要再次处理一下
        return HttpResponse(json.dumps({'data_l': page_infos, 'all_count': all_count}), content_type='json')
