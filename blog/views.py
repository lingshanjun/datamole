# coding=utf-8
from django.shortcuts import render
from .models import BlogType, Blog, BlogBigType
from django.http import HttpResponseServerError


def blogList(request):
    """blog列表页"""
    data = {}
    type =  request.REQUEST.get('type', None) #原创或转载
    category = request.REQUEST.get('category', None) # 分类
    blogs = Blog.objects.exclude(status=0).order_by('-id')  # blog列表

    if type == 'create':
        blogs = blogs.filter(origin=0)
    elif type == 'copy':
        blogs = blogs.filter(origin=1)

    if category is not None:
        blogs = blogs.filter(type=category)

    data['blogs'] = blogs
    data['bigtype'] = BlogBigType.objects.all().order_by('id')  # blog大分类
    data['hot'] = Blog.objects.exclude(status=0).order_by('-counts')[:10]  # blog 热门文章
    data['recomment'] = Blog.objects.exclude(status=0).filter(is_recomment=True).order_by('-id')[:10]  # blog 推荐文章
    return render(request, 'blog_list.html', data)


def blogDetail(request, id=None):
    """blog详细页面"""
    data = {}
    blog = Blog.objects.get(pk=id)

    if blog.status == 0:
        return HttpResponseServerError('文章不存在！')

    data['blog'] = blog
    data['bigtype'] = BlogBigType.objects.all().order_by('id')

    blog.counts += 1
    blog.save()

    authors = blog.authors.all()
    data['authors'] = authors

    return render(request, 'blog_detail.html', data)
