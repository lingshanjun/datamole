# coding=utf-8
from django.shortcuts import render
from blog.models import BlogType,Blog,BlogBigType
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseServerError

def blogList(request):
	"""blog列表页"""
	data ={}
	data['blog'] = Blog.objects.exclude(status=0).order_by('-id')	#blog列表
	data['bigtype'] = BlogBigType.objects.all().order_by('id')	#blog大分类
	data['hot'] = Blog.objects.exclude(status=0).order_by('-counts')[:10]	#blog 热门文章
	data['recomment'] = Blog.objects.exclude(status=0).filter(is_recomment=True).order_by('-id')[:10]	#blog 推荐文章
	return render(request, 'blog_list.html', data)


def type(request,id):
	"""根据分类获得blog列表页"""
	data ={}
	data['blog'] = Blog.objects.filter(type=id).exclude(status=0).order_by('-id')	#根据分类获得blog列表页
	data['bigtype'] = BlogBigType.objects.all().order_by('id')	#blog大分类
	data['hot'] = Blog.objects.exclude(status=0).order_by('-counts')[:10]	#blog 热门文章
	data['recomment'] = Blog.objects.exclude(status=0).filter(is_recomment=True).order_by('-id')[:10]	#blog 推荐文章
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
    return render(request, 'blog_detail.html', data)