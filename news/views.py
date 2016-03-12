# coding=utf-8
from django.shortcuts import render
from .models import  News
from django.http import HttpResponseServerError


def newsList(request):
    """news列表页"""
    data = {'newses': News.objects.order_by('-proirity')}

    return render(request, 'news_list.html', data)


def newsDetail(request, id=None):
    """news详情页"""
    data = {}
    news = News.objects.get(pk=id)
    data['news'] = news

    if not news:
        return HttpResponseServerError('新闻不存在！')

    return render(request, 'news_detail.html', data)
