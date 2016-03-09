# coding=utf-8
from django.shortcuts import render
from blog.models import BlogType,Blog,BlogBigType
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseServerError

def datamoleIndex(request):
	"""datamole首页"""
	data ={}
	# data['blog'] = Blog.objects.exclude(status=0).order_by('-id')	#blog列表
	# data['bigtype'] = BlogBigType.objects.all().order_by('id')	#blog大分类
	# data['hot'] = Blog.objects.exclude(status=0).order_by('-counts')[:10]	#blog 热门文章
	# data['recomment'] = Blog.objects.exclude(status=0).filter(is_recomment=True).order_by('-id')[:10]	#blog 推荐文章
	return render(request, 'datamole_index.html', data)