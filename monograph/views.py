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
            ch = {}
            sections = MonoSection.objects.filter(chapter=chapter.id).order_by('order')
            ch['title'] = chapter.title
            ch['order'] = chapter.order
            ch['sections'] = sections

            data['chapters'].append(ch)

    if 'corder' in request.GET:
        corder = request.GET['corder']
        chapter_detail = MonoChapter.objects.get(order=int(corder))
        data['chapter_detail'] = chapter_detail

    if 'sorder' in request.GET:
        sorder = request.GET['sorder']
        section_detail = MonoSection.objects.get(order=float(sorder))
        data['section_detail'] = section_detail

    return render(request, 'monograph_detail.html', data)
