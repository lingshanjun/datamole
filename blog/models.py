# coding=utf-8
from django.db import models
from django.utils.html import format_html


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
    title = models.CharField('标题', max_length=100, help_text='*必填*')
    type = models.ForeignKey(BlogType, verbose_name=u'所属分类', help_text='*必填*')
    cover = models.ImageField('封面图', null= True, upload_to='blog/')  # 博客导图
    content_show = models.TextField('正文显示', null= True)
    add_date = models.DateTimeField('创建日期', auto_now_add=True)
    counts = models.IntegerField('点击数', default=0)  # 热度
    is_recomment = models.BooleanField('推荐', default=False)
    status = models.SmallIntegerField('编辑状态', choices=STATUS, default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'blog_detail'
        verbose_name = '博客详情'
        verbose_name_plural = '博客详情'

    def get_summery(self):
        """获取该blog的摘要"""
        summary = self.content_show[:10]
        return summary

    get_summery.short_description = '摘要'

    def show_cover(self):
        """显示封面图"""
        return format_html('<a href="{0}"> <img src="{0}" width="60" height="auto"></a>', self.cover.url)

    show_cover.short_description = '封面'
    show_cover.allow_tags = True

    def get_absolute_url(self):
        """在站点查看该blog--admin默认"""
        return '/blog/%s' % self.id

    def show_blog_onsite(self):
        """在站点查看该blog--自定义"""
        return format_html('<a href="/blog/{}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>',
                           self.id)

    show_blog_onsite.short_description = '在站点查看'
    show_blog_onsite.allow_tags = True
