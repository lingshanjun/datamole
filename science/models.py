# -*- coding:utf-8 -*-

from django.db import models
from member.models import Member
from django.utils.html import format_html


class Paper(models.Model):
    title = models.CharField('题目', max_length=50, help_text='*必填*')
    abstract = models.TextField('摘要', help_text='*必填*')
    authors = models.ManyToManyField(Member, verbose_name=u'作者', blank=True, help_text='*必填*, 在列表中选择包含的作者')
    all_authors = models.CharField('所有作者', max_length=50, help_text='*必填*, 请按顺序输入所有作者笔名，如“张三，李四，王五”')
    pub_time = models.DateField('发表时间', help_text='*必填*')
    pub_location = models.CharField('发表地点', blank=True, max_length=50)
    pub_pulications = models.CharField('发表刊物', blank=True, max_length=50)
    link = models.URLField('公开链接', max_length=200, help_text="*必填*, 例如 https://www.baidu.com/")
    is_download = models.BooleanField('允许下载', default=False)
    dl_file = models.FileField('供下载的文件', blank=True, upload_to='paper/download/')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'paper'
        verbose_name = '论文'
        verbose_name_plural = '论文'

    def get_summery(self):
        """摘要"""
        return self.abstract[:20]

    get_summery.short_description = '摘要'

    def author_in_member(self):
        members = Paper.objects.get(pk=self.id).authors.all()

        html_str = []
        for obj in members:
            html_str.append(obj.name)

        html_str = ','.join(html_str)
        
        return html_str

    author_in_member.short_description = '成员作者'
    author_in_member.allow_tags = True

    def get_absolute_url(self):
        """在站点查看该论文--admin默认"""
        return '/science/paper/%s' % self.id

    def show_paper_onsite(self):
        """在站点查看该论文--自定义"""
        return format_html(
            '<a href="/science/paper/{}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>', self.id)

    show_paper_onsite.short_description = '在站点查看'
    show_paper_onsite.allow_tags = True
