# -*- coding:utf-8 -*-

from django.db import models
from django.utils.html import format_html

class Member(models.Model):
	SEX =[
		(0,'保密'),
		(1,'男'),
		(2,'女'),
	]
	WORK_STATUS = [
		(0,'离职'),
		(1,'在职'),
	]
	name = models.CharField('姓名',max_length=10)
	sex = models.SmallIntegerField('性别',choices=SEX,default=0)
	avatar = models.FileField('头像',blank=True,upload_to='team/')
	descripe = models.TextField('简介',default='一句话介绍自己')
	birthday = models.DateField('生日',blank=True)
	qq = models.CharField('QQ',max_length=15,blank=True)
	wechat = models.CharField('微信',max_length=50,blank=True)
	weibo = models.CharField('微博',max_length=50,blank=True)
	email = models.EmailField('邮箱',blank=True)

	jionin = models.DateField('加入时间')
	work_status = models.SmallIntegerField('在职状态',choices=WORK_STATUS,default=1)
	search = models.CharField('研究方向',max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'member'
		verbose_name = '成员列表'
		verbose_name_plural = '成员列表'

	def get_summery(self):
		"""获取该成员的简介"""
		return self.descripe[:20]

	get_summery.short_description = '简介'

	def show_cover(self):
		"""显示该成员头像"""
		return format_html('<a href="{0}"> <img src="{0}" width="60" height="auto"></a>', self.avatar)

	show_cover.short_description = '头像'
	show_cover.allow_tags = True

	def get_absolute_url(self):
		"""在站点查看该成员--admin默认"""
		return '/member/%s' % self.id

	def show_member_onsite(self):
		"""在站点查看该成员--自定义"""
		return format_html('<a href="/member/{}" target="_blank"><i class="glyphicon glyphicon-eye-open"></i></a>', self.id)

	show_member_onsite.short_description = '在站点查看'
	show_member_onsite.allow_tags = True
