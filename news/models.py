# -*- coding:utf-8 -*-

from django.db import models
from django.utils.html import format_html


class News(models.Model):
    title = models.CharField('新闻标题', max_length=50, help_text='*必填*')
    news_descripe = models.TextField('新闻内容', help_text='*必填*')
    proirity = models.SmallIntegerField('优先级编号', default=0, help_text='*必填*, 为整数,从0开始,数越大,优先级越高')
    time = models.DateField('发生时间', blank=True)
    add_time = models.DateField('创建时间', auto_now_add=True)
    cover = models.ImageField('封面', blank=True, upload_to='news/cover/')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = '新闻列表'
        verbose_name_plural = '新闻列表'

    def get_summery(self):
        """内容"""
        return self.news_descripe[:20]

    get_summery.short_description = '内容'

    def show_cover(self):
        """显示该新闻封面"""
        return format_html('<a href="{0}"> <img src="{0}" width="60" height="auto"></a>', self.cover.url)

    show_cover.short_description = ' 封面'
    show_cover.allow_tags = True

    def get_absolute_url(self):
        """在站点查看该新闻--admin默认"""
        return '/news/%s' % self.id

    def show_news_onsite(self):
        """在站点查看该新闻--自定义"""
        return format_html(
            '<a href="/news/{}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>', self.id)

    show_news_onsite.short_description = '在站点查看'
    show_news_onsite.allow_tags = True