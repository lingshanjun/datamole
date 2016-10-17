# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from others.models import Recruit


def datamoleIndex(request):
    """datamole首页"""
    data = {}
    recruit = Recruit.objects.filter(is_show=True).order_by('-add_date').all()

    if recruit:
        data['recruit'] = recruit[0]

    return render(request, 'datamole_index.html', data)


def introduce(request):
    """介绍实验室的详细页面"""
    data = {}
    return render(request, 'datamole_introduce.html', data)
