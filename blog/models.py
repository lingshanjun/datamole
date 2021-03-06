# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from HTMLParser import HTMLParser
from member.models import Member

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

from datamole.settings.safe_data import cloudinary_data

cloudinary.config(
    cloud_name=cloudinary_data['cloud_name'],
    api_key=cloudinary_data['api_key'],
    api_secret=cloudinary_data['api_secret']
)


class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print 'tag', tag
        print 'attrs', attrs


class BlogBigType(models.Model):
    """博客大分类"""

    name = models.CharField('大分类名', max_length=50, help_text='*必填*')
    add_date = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'blog_bigtype'
        verbose_name = '博客大分类'
        verbose_name_plural = '博客大分类'

    def getType(self):
        # 获取各大分类下的小分类
        return BlogType.objects.filter(bigtype=self.id)


class BlogType(models.Model):
    """博客分类"""

    name = models.CharField('分类名', max_length=50, help_text='*必填*')
    add_date = models.DateTimeField('创建时间', auto_now_add=True)
    bigtype = models.ForeignKey(BlogBigType, verbose_name=u'所属大分类', help_text='*必填*')

    def __unicode__(self):
        return self.name

    def getCount(self):
        """获取改分类下blog的数目"""
        return Blog.objects.exclude(status=0).filter(type=self.id).count()

    class Meta:
        db_table = 'blog_type'
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'


class Blog(models.Model):
    """博客详情"""

    STATUS = [
        (0, '草稿'),
        (1, '发布'),
    ]
    ORIGIN = [
        (0, '原创'),
        (1, '转载'),
    ]
    title = models.CharField('标题', max_length=100, help_text='*必填*')
    type = models.ForeignKey(BlogType, verbose_name=u'所属分类', help_text='*必填*')
    # cover = models.ImageField('封面图', null= True, upload_to='blog/', blank=True)  # 博客导图
    cover = CloudinaryField('封面图', null= True, blank=True)
    abstract = models.TextField('简介', help_text='*必填*', null=True)
    content_show = models.TextField('正文显示', null= True)
    add_date = models.DateTimeField('创建日期', auto_now_add=True)
    counts = models.IntegerField('点击数', default=0)  # 热度
    is_recomment = models.BooleanField('推荐', default=False)
    status = models.SmallIntegerField('编辑状态', choices=STATUS, default=0)
    origin = models.SmallIntegerField('是否原创', choices=ORIGIN, default=0)
    authors = models.ManyToManyField(Member, verbose_name=u'作者', blank=True, help_text='在列表中选择包含的作者')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'blog_detail'
        verbose_name = '博客详情'
        verbose_name_plural = '博客详情'

    def show_cover(self):
        """显示封面图"""
        if self.cover:
            cover_src = self.cover.url
            return format_html('<a href="{0}" target="_blank"> <img src="{0}" width="60" height="auto"></a>', cover_src)
        else:
            return u'无'

    show_cover.short_description = '封面'
    show_cover.allow_tags = True

    # def get_cover(self):
    #     """获取封面图
    #         若上传封面图,则此即为封面图;
    #         若文章中也没有插图,则选择默认的图片为封面图
    #     """
    #     if self.cover:
    #         cover_src = self.cover.url
    #     else:
    #         cover_src = '/static/common/img/default.png'
    #
    #     return cover_src

    def author_in_member(self):
        members = Blog.objects.get(pk=self.id).authors.all()

        html_str = []
        if members:
            for obj in members:
                html_obj = format_html('<a href="{0}" target="_blank">{1}</a>', obj.get_absolute_url(), obj.name)
                html_str.append(html_obj)
        else:
            html_str.append('datamole') # 默认

        html_str = ','.join(html_str)

        return html_str

    author_in_member.short_description = '作者'
    author_in_member.allow_tags = True

    def get_absolute_url(self):
        """在站点查看该blog--admin默认"""
        return '/blog/%s' % self.id

    def show_blog_onsite(self):
        """在站点查看该blog--自定义"""
        return format_html('<a href="/blog/{}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>',
                           self.id)

    show_blog_onsite.short_description = '在站点查看'
    show_blog_onsite.allow_tags = True
