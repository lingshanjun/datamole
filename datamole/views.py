# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError


def datamoleIndex(request):
    """datamole首页"""
    data = {}
    return render(request, 'datamole_index.html', data)
