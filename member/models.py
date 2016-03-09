# -*- coding:utf-8 -*-

from django.db import models

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
