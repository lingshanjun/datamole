# coding=utf-8
from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseServerError

def memberList(request):
	"""member首页"""
	data ={}
	data['members'] = Member.objects.order_by('id')
	return render(request, 'member_list.html', data)


def memberDetail(request, id=None):
    """member详细页面"""
    data = {}
    member = Member.objects.get(pk=id)

    data['member'] = member

    return render(request, 'member_detail.html', data)