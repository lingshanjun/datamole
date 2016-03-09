# coding=utf-8
"""datamole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'datamole.views.datamoleIndex', name='index'), #网站首页

    url(r'^blog/$', 'blog.views.blogList', name='blog_list'), #教程列表
    url(r'^blog/type/(?P<id>\d+)/$', 'blog.views.type', name='blog_type'), #教程列表（根据分类显示）
    url(r'^blog/(?P<id>\d+)/$', 'blog.views.blogDetail', name='blog_detail'), #教程列表（根据标签显示）
]
