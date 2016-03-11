# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160310_1826'),
        ('science', '0007_auto_20160310_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=50, verbose_name=b'\xe4\xb8\x93\xe5\x88\xa9\xe5\x90\x8d\xe7\xa7\xb0')),
                ('descripe', models.TextField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe4\xb8\x93\xe5\x88\xa9\xe6\x8f\x8f\xe8\xbf\xb0\xef\xbc\x88\xe6\x91\x98\xe8\xa6\x81\xef\xbc\x89')),
                ('all_creators', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe8\xaf\xb7\xe6\x8c\x89\xe9\xa1\xba\xe5\xba\x8f\xe8\xbe\x93\xe5\x85\xa5\xe6\x89\x80\xe6\x9c\x89\xe5\x8f\x91\xe6\x98\x8e\xe4\xba\xba\xe7\xac\x94\xe5\x90\x8d\xef\xbc\x8c\xe5\xa6\x82\xe2\x80\x9c\xe5\xbc\xa0\xe4\xb8\x89\xef\xbc\x8c\xe6\x9d\x8e\xe5\x9b\x9b\xef\xbc\x8c\xe7\x8e\x8b\xe4\xba\x94\xe2\x80\x9d', max_length=50, verbose_name=b'\xe6\x89\x80\xe6\x9c\x89\xe5\x8f\x91\xe6\x98\x8e\xe4\xba\xba')),
                ('status', models.SmallIntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'apply', b'\xe7\x94\xb3\xe8\xaf\xb7'), (b'open', b'\xe5\x85\xac\xe5\xbc\x80'), (b'enpower', b'\xe6\x8e\x88\xe6\x9d\x83')])),
                ('num_apply', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe5\x8f\xb7', blank=True)),
                ('num_open', models.CharField(max_length=50, verbose_name=b'\xe5\x85\xac\xe5\xbc\x80\xe5\x8f\xb7', blank=True)),
                ('num_enpower', models.CharField(max_length=50, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe5\x8f\xb7', blank=True)),
                ('time_apply', models.DateField(verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('time_open', models.DateField(verbose_name=b'\xe5\x85\xac\xe5\xbc\x80\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('time_enpower', models.DateField(verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('link', models.URLField(help_text=b'\xe4\xbe\x8b\xe5\xa6\x82 https://www.baidu.com/', verbose_name=b'\xe5\x85\xac\xe5\xbc\x80\xe9\x93\xbe\xe6\x8e\xa5')),
                ('creators', models.ManyToManyField(help_text=b'\xe5\x9c\xa8\xe5\x88\x97\xe8\xa1\xa8\xe4\xb8\xad\xe9\x80\x89\xe6\x8b\xa9\xe5\x8c\x85\xe5\x90\xab\xe7\x9a\x84\xe5\x8f\x91\xe6\x98\x8e\xe4\xba\xba', to='member.Member', verbose_name='\u53d1\u660e\u4eba', blank=True)),
            ],
            options={
                'db_table': 'patent',
                'verbose_name': '\u4e13\u5229',
                'verbose_name_plural': '\u4e13\u5229',
            },
        ),
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(help_text=b'\xe5\x9c\xa8\xe5\x88\x97\xe8\xa1\xa8\xe4\xb8\xad\xe9\x80\x89\xe6\x8b\xa9\xe5\x8c\x85\xe5\x90\xab\xe7\x9a\x84\xe4\xbd\x9c\xe8\x80\x85', to='member.Member', verbose_name='\u4f5c\u8005', blank=True),
        ),
    ]
