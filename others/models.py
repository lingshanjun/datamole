# -*- coding:utf-8 -*-

from django.db import models
from django.utils.html import format_html


class Recruit(models.Model):
    title = models.CharField('标题', max_length=100, help_text='*必填*,不在主页显示,用于标记各条招贤令内容')
    recruit_content = models.TextField('招聘内容', help_text='*必填*')
    is_show = models.BooleanField('首页显示', default=False, help_text="首页只能显示一条招贤令内容,当且仅当该项选中时,该条招贤令才可在首页正确显示.")
    add_date = models.DateTimeField('创建日期', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'recruit'
        verbose_name = '招贤令'
        verbose_name_plural = '招贤令'
