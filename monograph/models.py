# coding=utf-8
from django.db import models
from django.utils.html import format_html, format_html_join
from member.models import Member


class MonoCover(models.Model):
    name = models.CharField('封面名称', max_length=100, help_text='*必填*, 用于提示该封面图片属于哪个专著,例如,"专著名-封面名-优先级"')
    priority = models.SmallIntegerField('优先级', default=0, help_text='*必填*, 从0开始的整数,用于设置封面图的顺序,数越大,优先级越高,默认为0')
    add_time = models.DateField('创建时间', auto_now_add=True)
    img = models.ImageField('图片', upload_to='monograph/cover/')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'monograph_cover'
        verbose_name = '专著封面图'
        verbose_name_plural = '专著封面图'

    def show_img(self):
        """显示该封面图片"""
        return format_html('<a href="{0}"> <img src="{0}" width="60" height="auto"></a>', self.img.url)

    show_img.short_description = '图片'
    show_img.allow_tags = True


class MonoBuy(models.Model):
    name = models.CharField('链接名称', max_length=100, help_text='*必填*, 用于提示该购买链接属于哪个专著,例如,"专著名-链接名-优先级"')
    link = models.URLField('购买链接', help_text='*必填*')
    priority = models.SmallIntegerField('优先级', default=0, help_text='*必填*, 从0开始的整数,用于设置链接的顺序,数越大,优先级越高,默认为0')
    add_time = models.DateField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'monograph_buy'
        verbose_name = '购买链接'
        verbose_name_plural = '购买链接'

    def show_link(self):
        """使链接可点击"""
        return format_html(
            '<a href="{0}" target="_blank">{0}</a>', self.link)

    show_link.short_description = '购买链接'
    show_link.allow_tags = True


class MonoList(models.Model):
    title = models.CharField('专著名称', max_length=50, help_text='*必填*')
    monolist_abstract = models.TextField('描述', help_text='*必填*')
    authors = models.ManyToManyField(Member, verbose_name=u'作者', help_text='在列表中选择包含的作者', blank=True)
    all_authors = models.CharField('所有作者', max_length=50, help_text='*必填*, 请按顺序输入所有作者笔名，如“张三，李四，王五”')
    pub_time = models.DateField('出版时间', help_text='*必填*')
    pub_pulications = models.CharField('出版社', blank=True, max_length=50)
    covers = models.ManyToManyField(MonoCover, verbose_name=u'封面图', blank=True)
    buys = models.ManyToManyField(MonoBuy, verbose_name=u'购买链接', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'monograph_list'
        verbose_name = '专著列表'
        verbose_name_plural = '专著列表'

    def author_in_member(self):
        members = MonoList.objects.get(pk=self.id).authors.all()

        html_str = []
        for obj in members:
            html_obj = format_html('<a href="{0}" target="_blank">{1}</a>', obj.get_absolute_url(), obj.name)
            html_str.append(html_obj)

        html_str = ','.join(html_str)

        return html_str

    author_in_member.short_description = '成员作者'
    author_in_member.allow_tags = True

    def show_covers(self):
        covers = MonoList.objects.get(pk=self.id).covers.all().order_by('-priority')

        html_str = []
        for obj in covers:
            html_obj = format_html(u'<a href="{0}" target="_blank">'
                                   u'<img src="{0}" width="60" height="auto" title="{1}">'
                                   u'</a>', obj.img.url, obj.name)
            html_str.append(html_obj)

        html_str = ' '.join(html_str)

        return html_str

    show_covers.short_description = '封面'
    show_covers.allow_tags = True

    def show_buys(self):
        buys = MonoList.objects.get(pk=self.id).buys.all().order_by('-priority')

        html_str = []
        for obj in buys:
            html_obj = format_html(u'<a href="{0}" target="_blank">{1}</a>', obj.link, obj.name)
            html_str.append(html_obj)

        html_str = '<br/>'.join(html_str)

        return html_str

    show_buys.short_description = '购买链接'
    show_buys.allow_tags = True

    def get_absolute_url(self):
        """在站点查看该专著--admin默认"""
        return '/monograph/%s' % self.id

    def show_monograph_onsite(self):
        """在站点查看该专著--自定义"""
        return format_html(
            '<a href="/monograph/{0}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>', self.id)

    show_monograph_onsite.short_description = '在站点查看'
    show_monograph_onsite.allow_tags = True


class MonoChapter(models.Model):
    order = models.SmallIntegerField('章序号', help_text="*必填*, 为整数,严格安装此格式,'0','1','2'等")
    title = models.CharField('章标题', max_length=100, help_text='*必填*')
    list = models.ForeignKey(MonoList, verbose_name=u'所属专著', help_text='*必填*')
    mono_chapter_content = models.TextField('本章介绍', help_text='可在此处编辑本章的介绍内容', blank=True)
    add_time = models.DateField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return u'专著%s 第%s章 %s' % (self.list.id, self.order, self.title)

    class Meta:
        db_table = 'monograph_chapter'
        verbose_name = '专著章列表'
        verbose_name_plural = '专著章列表'

    def show_list(self):
        return self.list

    show_list.short_description = '所属专著'


class MonoSection(models.Model):
    order = models.DecimalField('节序号', max_digits=2, decimal_places=1,
                                help_text='*必填*, 只支持二级标题的序号，如1.1，2.3，不支持其它级标题，如1.1.2，3.4.2.1等')
    title = models.CharField('节标题', max_length=100, help_text='*必填*')
    chapter = models.ForeignKey(MonoChapter, verbose_name=u'所属章目录', help_text='*必填*')
    mono_section_content = models.TextField('具体内容', blank=True, help_text='可在此处编辑每章的具体内容,注意:')
    add_time = models.DateField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'monograph_section'
        verbose_name = '专著节列表'
        verbose_name_plural = '专著节列表'

    def show_list(self):
        return self.chapter.list

    show_list.short_description = '所属专著'

    def show_chapter(self):
        return u'第%s章 %s' % (self.chapter.order, self.chapter.title)

    show_chapter.short_description = '所属章'