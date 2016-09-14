# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from news.models import Slide


def datamoleIndex(request):
    """datamole首页"""
    data = {}
    slides = Slide.objects.order_by('priority').all()
    data['slides'] = slides
    return render(request, 'datamole_index.html', data)
