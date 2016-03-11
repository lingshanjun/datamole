# coding=utf-8
from django.shortcuts import render
from .models import Member
from django.http import HttpResponseServerError


def memberList(request):
    """member首页"""
    data = {'members': Member.objects.order_by('id')}
    return render(request, 'member_list.html', data)


def memberDetail(request, id=None):
    """member详细页面
    :param id:
    """
    data = {}
    member = Member.objects.get(pk=id)

    data['member'] = member

    if not member:
        return HttpResponseServerError('成员不存在！')

    return render(request, 'member_detail.html', data)
