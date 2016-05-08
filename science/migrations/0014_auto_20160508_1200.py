# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0013_auto_20160508_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='paper_article',
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(help_text='*\u5fc5\u586b*', verbose_name='\u6458\u8981'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='all_authors',
            field=models.CharField(help_text='*\u5fc5\u586b*, \u8bf7\u6309\u987a\u5e8f\u8f93\u5165\u6240\u6709\u4f5c\u8005\u7b14\u540d\uff0c\u5982\u201c\u5f20\u4e09\uff0c\u674e\u56db\uff0c\u738b\u4e94\u201d', max_length=50, verbose_name='\u6240\u6709\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(help_text='\u5728\u5217\u8868\u4e2d\u9009\u62e9\u5305\u542b\u7684\u4f5c\u8005', to='member.Member', verbose_name='\u4f5c\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='dl_file',
            field=models.FileField(upload_to='paper/download/', verbose_name='\u4f9b\u4e0b\u8f7d\u7684\u6587\u4ef6', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='is_download',
            field=models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u4e0b\u8f7d'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='key_words',
            field=models.CharField(default='', help_text='*\u5fc5\u586b*, \u7528\u9017\u53f7\u9694\u5f00', max_length=100, verbose_name='\u5173\u952e\u5b57'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.URLField(help_text='*\u5fc5\u586b*, \u4f8b\u5982 https://www.baidu.com/', verbose_name='\u516c\u5f00\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pub_location',
            field=models.CharField(max_length=50, verbose_name='\u53d1\u8868\u5730\u70b9', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pub_pulications',
            field=models.CharField(max_length=50, verbose_name='\u53d1\u8868\u520a\u7269', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pub_time',
            field=models.DateField(help_text='*\u5fc5\u586b*', verbose_name='\u53d1\u8868\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(help_text='*\u5fc5\u586b*', max_length=50, verbose_name='\u9898\u76ee'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='all_creators',
            field=models.CharField(help_text='*\u5fc5\u586b*, \u8bf7\u6309\u987a\u5e8f\u8f93\u5165\u6240\u6709\u53d1\u660e\u4eba\u7b14\u540d\uff0c\u5982\u201c\u5f20\u4e09\uff0c\u674e\u56db\uff0c\u738b\u4e94\u201d', max_length=50, verbose_name='\u6240\u6709\u53d1\u660e\u4eba'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='creators',
            field=models.ManyToManyField(help_text='\u5728\u5217\u8868\u4e2d\u9009\u62e9\u5305\u542b\u7684\u53d1\u660e\u4eba', to='member.Member', verbose_name='\u53d1\u660e\u4eba', blank=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='descripe',
            field=models.TextField(help_text='*\u5fc5\u586b*', verbose_name='\u4e13\u5229\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='link',
            field=models.URLField(help_text='\u4f8b\u5982 https://www.baidu.com/', verbose_name='\u516c\u5f00\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='num_apply',
            field=models.CharField(max_length=50, verbose_name='\u7533\u8bf7\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='num_enpower',
            field=models.CharField(max_length=50, verbose_name='\u6388\u6743\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='num_open',
            field=models.CharField(max_length=50, verbose_name='\u516c\u5f00\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='status',
            field=models.SmallIntegerField(help_text='*\u5fc5\u586b*', verbose_name='\u72b6\u6001', choices=[(2, '\u516c\u5f00'), (3, '\u6388\u6743'), (1, '\u7533\u8bf7')]),
        ),
        migrations.AlterField(
            model_name='patent',
            name='time_apply',
            field=models.DateField(verbose_name='\u7533\u8bf7\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='time_enpower',
            field=models.DateField(verbose_name='\u6388\u6743\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='time_open',
            field=models.DateField(verbose_name='\u516c\u5f00\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='title',
            field=models.CharField(help_text='*\u5fc5\u586b*', max_length=50, verbose_name='\u4e13\u5229\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='all_persons',
            field=models.CharField(help_text='*\u5fc5\u586b*, \u8bf7\u6309\u987a\u5e8f\u8f93\u5165\u6240\u6709\u53d1\u660e\u4eba\u7b14\u540d\uff0c\u5982\u201c\u5f20\u4e09\uff0c\u674e\u56db\uff0c\u738b\u4e94\u201d', max_length=50, verbose_name='\u6240\u6709\u83b7\u5956\u4eba'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='cover',
            field=models.ImageField(upload_to='prize/cover/', verbose_name='\u5c01\u9762\u56fe', blank=True),
        ),
        migrations.AlterField(
            model_name='prize',
            name='grade',
            field=models.SmallIntegerField(help_text='*\u5fc5\u586b*', verbose_name='\u5956\u9879\u7ea7\u522b', choices=[(1, '\u56fd\u9645\u7ea7'), (2, '\u56fd\u5bb6\u7ea7'), (3, '\u7701\u5e02\u7ea7'), (4, '\u6821\u7ea7'), (0, '\u5176\u5b83')]),
        ),
        migrations.AlterField(
            model_name='prize',
            name='persons',
            field=models.ManyToManyField(help_text='\u5728\u5217\u8868\u4e2d\u9009\u62e9\u5305\u542b\u7684\u53d1\u660e\u4eba', to='member.Member', verbose_name='\u83b7\u5956\u4eba'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='prize_descripe',
            field=models.TextField(help_text='*\u5fc5\u586b*', verbose_name='\u5185\u5bb9\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='time',
            field=models.DateField(verbose_name='\u83b7\u5956\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='prize',
            name='title',
            field=models.CharField(help_text='*\u5fc5\u586b*', max_length=50, verbose_name='\u83b7\u5956\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='soft',
            name='all_creators',
            field=models.CharField(help_text='*\u5fc5\u586b*, \u8bf7\u6309\u987a\u5e8f\u8f93\u5165\u6240\u6709\u53d1\u660e\u4eba\u7b14\u540d\uff0c\u5982\u201c\u5f20\u4e09\uff0c\u674e\u56db\uff0c\u738b\u4e94\u201d', max_length=50, verbose_name='\u6240\u6709\u53d1\u660e\u4eba'),
        ),
        migrations.AlterField(
            model_name='soft',
            name='creators',
            field=models.ManyToManyField(help_text='\u5728\u5217\u8868\u4e2d\u9009\u62e9\u5305\u542b\u7684\u53d1\u660e\u4eba', to='member.Member', verbose_name='\u53d1\u660e\u4eba'),
        ),
        migrations.AlterField(
            model_name='soft',
            name='descripe',
            field=models.TextField(help_text='*\u5fc5\u586b*', verbose_name='\u8f6f\u8457\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='soft',
            name='number',
            field=models.CharField(max_length=50, verbose_name='\u7f16\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='soft',
            name='pic',
            field=models.ImageField(upload_to='soft/pic/', verbose_name='\u8bc1\u4e66\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='soft',
            name='time',
            field=models.DateField(verbose_name='\u9996\u6b21\u53d1\u8868\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='soft',
            name='title',
            field=models.CharField(help_text='*\u5fc5\u586b*', max_length=50, verbose_name='\u8f6f\u8457\u540d\u79f0'),
        ),
    ]
