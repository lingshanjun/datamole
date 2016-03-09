# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('sex', models.SmallIntegerField(default=0, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe4\xbf\x9d\xe5\xaf\x86'), (1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')])),
                ('avatar', models.FileField(upload_to=b'team/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
                ('descripe', models.TextField(default=b'\xe4\xb8\x80\xe5\x8f\xa5\xe8\xaf\x9d\xe4\xbb\x8b\xe7\xbb\x8d\xe8\x87\xaa\xe5\xb7\xb1', verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5', blank=True)),
                ('qq', models.CharField(max_length=15, verbose_name=b'QQ', blank=True)),
                ('wechat', models.CharField(max_length=50, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1', blank=True)),
                ('weibo', models.CharField(max_length=50, verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('jionin', models.DateField(verbose_name=b'\xe5\x8a\xa0\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4')),
                ('work_status', models.SmallIntegerField(default=1, verbose_name=b'\xe5\x9c\xa8\xe8\x81\x8c\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe7\xa6\xbb\xe8\x81\x8c'), (1, b'\xe5\x9c\xa8\xe8\x81\x8c')])),
                ('search', models.CharField(max_length=100, verbose_name=b'\xe7\xa0\x94\xe7\xa9\xb6\xe6\x96\xb9\xe5\x90\x91')),
            ],
            options={
                'db_table': 'member',
                'verbose_name': '\u6210\u5458',
                'verbose_name_plural': '\u6210\u5458',
            },
        ),
    ]
