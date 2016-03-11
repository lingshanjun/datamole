# coding=utf-8
from django.shortcuts import render
from .models import Paper
from django.http import HttpResponseServerError


def paperList(request):
    """paper列表页"""
    data = {'papers': Paper.objects.order_by('-pub_time')}

    return render(request, 'paper_list.html', data)


def paperDetail(request, id=None):
    """paper详情页"""
    data = {}
    paper = Paper.objects.get(pk=id)
    data['paper'] = paper

    if not paper:
        return HttpResponseServerError('论文不存在！')

    return render(request, 'paper_detail.html', data)
