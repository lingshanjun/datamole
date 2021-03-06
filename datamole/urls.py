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
from django.conf.urls.static import static
from django.conf import settings
from tools.upload import file_upload

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'datamole.views.datamoleIndex', name='index'),  # 网站首页

    url(r'^introduce/$', 'datamole.views.introduce', name='introduce'),  # 实验室介绍页面

    url(r'^blog/$', 'blog.views.blogList', name='blog_list'),  # 教程列表
    url(r'^blog/(?P<id>\d+)/$', 'blog.views.blogDetail', name='blog_detail'),  # 教程详情

    url(r'^member/$', 'member.views.memberList', name='member_list'),  # 成员列表
    url(r'^member/(?P<id>\d+)/$', 'member.views.memberDetail', name='member_detail'),  # 成员详情

    url(r'^science/paper/$', 'science.views.paperList', name='paper_list'),  # 论文列表
    url(r'^science/paper/(?P<id>\d+)/$', 'science.views.paperDetail', name='paper_detail'),  # 论文详情

    url(r'^science/patent/$', 'science.views.patentList', name='patent_list'),  # 专利列表
    url(r'^science/patent/(?P<id>\d+)/$', 'science.views.patentDetail', name='patent_detail'),  # 专利详情

    url(r'^science/soft/$', 'science.views.softList', name='soft_list'),  # 软著列表
    url(r'^science/soft/(?P<id>\d+)/$', 'science.views.softDetail', name='soft_detail'),  # 软著详情

    url(r'^science/prize/$', 'science.views.prizeList', name='prize_list'),  # 获奖列表
    url(r'^science/prize/(?P<id>\d+)/$', 'science.views.prizeDetail', name='prize_detail'),  # 获奖详情

    url(r'^news/$', 'news.views.newsList', name='news_list'),  # 新闻列表
    url(r'^news/(?P<id>\d+)/$', 'news.views.newsDetail', name='news_detail'),  # 新闻详情

    url(r'^monograph/(?P<id>\d+)/$', 'monograph.views.monographDetail', name='monograph_detail'),  # 专著详情

    url(r'^upload/', file_upload),  # upload file with simditor

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
