# coding=utf-8
from django.shortcuts import render
from .models import Paper, Patent, Soft, Prize
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


def patentList(request):
    """patent列表页"""
    data = {'patents': Patent.objects.order_by('-id')}

    return render(request, 'patent_list.html', data)


def softList(request):
    """soft列表页"""
    data = {'softs': Soft.objects.order_by('-id')}

    return render(request, 'soft_list.html', data)

def prizeList(request):
    """prize列表页"""
    data = {'prizes': Prize.objects.order_by('-time')}

    return render(request, 'prize_list.html', data)


def prizeDetail(request, id=None):
    """prize详情页"""
    data = {}
    prize = Prize.objects.get(pk=id)
    data['prize'] = prize

    if not prize:
        return HttpResponseServerError('获奖信息不存在！')

    return render(request, 'prize_detail.html', data)