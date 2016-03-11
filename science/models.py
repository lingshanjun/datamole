# -*- coding:utf-8 -*-

from django.db import models
from member.models import Member
from django.utils.html import format_html


class Paper(models.Model):
    title = models.CharField('题目', max_length=50, help_text='*必填*')
    abstract = models.TextField('摘要', help_text='*必填*')
    authors = models.ManyToManyField(Member, verbose_name=u'作者', blank=True, help_text='在列表中选择包含的作者')
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

    def show_link(self):
        """使链接可点击"""
        return format_html(
            '<a href="{0}" target="_blank">{0}</a>', self.link)


class Patent(models.Model):
    STATUS = {
        (1, '申请'),
        (2, '公开'),
        (3, '授权')
    }
    title = models.CharField('专利名称', max_length=50, help_text='*必填*')
    descripe = models.TextField('专利描述', help_text='*必填*')
    creators = models.ManyToManyField(Member, verbose_name=u'发明人', blank=True, help_text='在列表中选择包含的发明人')
    all_creators = models.CharField('所有发明人', max_length=50, help_text='*必填*, 请按顺序输入所有发明人笔名，如“张三，李四，王五”')
    status = models.SmallIntegerField('状态', choices=STATUS, help_text='*必填*')
    num_apply = models.CharField('申请号', max_length=50, blank=True)
    num_open = models.CharField('公开号', max_length=50, blank=True)
    num_enpower = models.CharField('授权号', max_length=50, blank=True)
    time_apply = models.DateField('申请时间', blank=True)
    time_open = models.DateField('公开时间', blank=True)
    time_enpower = models.DateField('授权时间', blank=True)
    link = models.URLField('公开链接', max_length=200, help_text='例如 https://www.baidu.com/')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'patent'
        verbose_name = '专利'
        verbose_name_plural = '专利'

    def get_summery(self):
        """专利描述"""
        return self.descripe[:20]

    get_summery.short_description = '摘要'

    def creator_in_member(self):
        members = Patent.objects.get(pk=self.id).creators.all()

        html_str = []
        for obj in members:
            html_str.append(obj.name)

        html_str = ','.join(html_str)

        return html_str

    creator_in_member.short_description = '成员发明人'
    creator_in_member.allow_tags = True

    def get_absolute_url(self):
        """在站点查看该专利--admin默认"""
        return '/science/patent/%s' % self.id

    def show_patent_onsite(self):
        """在站点查看该专利--自定义"""
        return format_html(
            '<a href="/science/patent/{0}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>', self.id)

    show_patent_onsite.short_description = '在站点查看'
    show_patent_onsite.allow_tags = True

    def show_link(self):
        """使链接可点击"""
        return format_html(
            '<a href="{0}" target="_blank">{0}</a>', self.link)


class Soft(models.Model):
    title = models.CharField('软著名称', max_length=50, help_text='*必填*')
    descripe = models.TextField('软著描述', help_text='*必填*')
    creators = models.ManyToManyField(Member, verbose_name=u'发明人', help_text='在列表中选择包含的发明人')
    all_creators = models.CharField('所有发明人', max_length=50, help_text='*必填*, 请按顺序输入所有发明人笔名，如“张三，李四，王五”')
    number = models.CharField('编号', max_length=50, blank=True)
    time = models.DateField('首次发表时间', blank=True)
    pic = models.ImageField('证书图片', blank=True, upload_to='soft/pic/')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'soft'
        verbose_name = '软著'
        verbose_name_plural = '软著'

    def get_summery(self):
        """软著描述"""
        return self.descripe[:20]

    get_summery.short_description = '摘要'

    def creator_in_member(self):
        members = Soft.objects.get(pk=self.id).creators.all()

        html_str = []
        for obj in members:
            html_str.append(obj.name)

        html_str = ','.join(html_str)

        return html_str

    creator_in_member.short_description = '成员发明人'
    creator_in_member.allow_tags = True

    def show_pic(self):
        """显示该软著证书图片"""
        return format_html('<a href="{0}"> <img src="{0}" width="60" height="auto"></a>', self.pic.url)

    show_pic.short_description = '证书图片'
    show_pic.allow_tags = True

    def get_absolute_url(self):
        """在站点查看该软著--admin默认"""
        return '/science/soft/%s' % self.id

    def show_soft_onsite(self):
        """在站点查看该软著--自定义"""
        return format_html(
            '<a href="/science/soft/{0}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>', self.id)

    show_soft_onsite.short_description = '在站点查看'
    show_soft_onsite.allow_tags = True