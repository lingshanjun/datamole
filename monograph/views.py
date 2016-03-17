# coding=utf-8
from django.shortcuts import render
from .models import  MonoCover, MonoBuy, MonoList, MonoChapter, MonoSection
from django.http import HttpResponseServerError


def monographDetail(request, id=None):
    """monograph详情页"""
    data = {}
    mono = MonoList.objects.get(pk=id)
    data['mono'] = mono

    if not mono:
        return HttpResponseServerError('专著不存在！')

    chapters = MonoChapter.objects.filter(list=mono.id).order_by('order')

    data['chapters'] = []

    if chapters:
        for chapter in chapters:
            chaper = {}
            sections = MonoSection.objects.filter(chapter=chapter.id).order_by('order')
            chaper['title'] = chapter.title
            chaper['order'] = chapter.order
            chaper['sections'] = sections

            data['chapters'].append(chaper)

    if 'sorder' in request.GET:
        sorder = request.GET['sorder']
        section = MonoSection.objects.get(order=float(sorder))
        if section:
            data['section'] = section

    return render(request, 'monograph_detail.html', data)
