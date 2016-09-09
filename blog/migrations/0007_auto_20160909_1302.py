# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160510_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='authors',
            field=models.ManyToManyField(help_text='\u5728\u5217\u8868\u4e2d\u9009\u62e9\u5305\u542b\u7684\u4f5c\u8005', to='member.Member', verbose_name='\u4f5c\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content_show',
            field=models.TextField(null=True, verbose_name='\u6b63\u6587\u663e\u793a'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='counts',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(upload_to='blog/', null=True, verbose_name='\u5c01\u9762\u56fe', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_recomment',
            field=models.BooleanField(default=False, verbose_name='\u63a8\u8350'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='origin',
            field=models.SmallIntegerField(default=0, verbose_name='\u662f\u5426\u539f\u521b', choices=[(0, '\u539f\u521b'), (1, '\u8f6c\u8f7d')]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.SmallIntegerField(default=0, verbose_name='\u7f16\u8f91\u72b6\u6001', choices=[(0, '\u8349\u7a3f'), (1, '\u53d1\u5e03')]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text='*\u5fc5\u586b*', max_length=100, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5206\u7c7b', to='blog.BlogType', help_text='*\u5fc5\u586b*'),
        ),
        migrations.AlterField(
            model_name='blogbigtype',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='blogbigtype',
            name='name',
            field=models.CharField(help_text='*\u5fc5\u586b*', max_length=50, verbose_name='\u5927\u5206\u7c7b\u540d'),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='bigtype',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5927\u5206\u7c7b', to='blog.BlogBigType', help_text='*\u5fc5\u586b*'),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='name',
            field=models.CharField(help_text='*\u5fc5\u586b*', max_length=50, verbose_name='\u5206\u7c7b\u540d'),
        ),
    ]
