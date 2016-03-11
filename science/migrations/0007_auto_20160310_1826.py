# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0006_auto_20160310_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe6\x91\x98\xe8\xa6\x81'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='all_authors',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe8\xaf\xb7\xe6\x8c\x89\xe9\xa1\xba\xe5\xba\x8f\xe8\xbe\x93\xe5\x85\xa5\xe6\x89\x80\xe6\x9c\x89\xe4\xbd\x9c\xe8\x80\x85\xe7\xac\x94\xe5\x90\x8d\xef\xbc\x8c\xe5\xa6\x82\xe2\x80\x9c\xe5\xbc\xa0\xe4\xb8\x89\xef\xbc\x8c\xe6\x9d\x8e\xe5\x9b\x9b\xef\xbc\x8c\xe7\x8e\x8b\xe4\xba\x94\xe2\x80\x9d', max_length=50, verbose_name=b'\xe6\x89\x80\xe6\x9c\x89\xe4\xbd\x9c\xe8\x80\x85'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe5\x9c\xa8\xe5\x88\x97\xe8\xa1\xa8\xe4\xb8\xad\xe9\x80\x89\xe6\x8b\xa9\xe5\x8c\x85\xe5\x90\xab\xe7\x9a\x84\xe4\xbd\x9c\xe8\x80\x85', to='member.Member', verbose_name='\u4f5c\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.URLField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe4\xbe\x8b\xe5\xa6\x82 https://www.baidu.com/', verbose_name=b'\xe5\x85\xac\xe5\xbc\x80\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pub_time',
            field=models.DateField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=50, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae'),
        ),
    ]
