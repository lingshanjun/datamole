# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=50, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe6\xa0\x87\xe9\xa2\x98')),
                ('news_descripe', models.TextField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe5\x86\x85\xe5\xae\xb9')),
                ('proirity', models.SmallIntegerField(default=0, help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe4\xb8\xba\xe6\x95\xb4\xe6\x95\xb0,\xe4\xbb\x8e0\xe5\xbc\x80\xe5\xa7\x8b,\xe6\x95\xb0\xe8\xb6\x8a\xe5\xa4\xa7,\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7\xe8\xb6\x8a\xe9\xab\x98', verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7\xe7\xbc\x96\xe5\x8f\xb7')),
                ('time', models.DateField(verbose_name=b'\xe5\x8f\x91\xe7\x94\x9f\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('add_time', models.DateField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('cover', models.ImageField(upload_to=b'news/cover/', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2', blank=True)),
            ],
            options={
                'db_table': 'news',
                'verbose_name': '\u65b0\u95fb\u5217\u8868',
                'verbose_name_plural': '\u65b0\u95fb\u5217\u8868',
            },
        ),
    ]
