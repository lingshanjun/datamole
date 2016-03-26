# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe7\x94\xa8\xe4\xba\x8e\xe6\x8f\x90\xe7\xa4\xba\xe8\xaf\xa5\xe8\xbd\xae\xe6\x92\xad\xe5\x9b\xbe\xe7\x89\x87\xe7\x9a\x84\xe4\xbf\xa1\xe6\x81\xaf', max_length=100, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x90\x8d\xe7\xa7\xb0')),
                ('priority', models.SmallIntegerField(default=0, help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe4\xbb\x8e0\xe5\xbc\x80\xe5\xa7\x8b\xe7\x9a\x84\xe6\x95\xb4\xe6\x95\xb0,\xe7\x94\xa8\xe4\xba\x8e\xe8\xae\xbe\xe7\xbd\xae\xe8\xbd\xae\xe6\x92\xad\xe5\x9b\xbe\xe7\x9a\x84\xe6\x92\xad\xe6\x94\xbe\xe9\xa1\xba\xe5\xba\x8f,\xe6\x95\xb0\xe8\xb6\x8a\xe5\xa4\xa7,\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7\xe8\xb6\x8a\xe9\xab\x98,\xe9\xbb\x98\xe8\xae\xa4\xe4\xb8\xba0', verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('img', models.ImageField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe5\xb0\xba\xe5\xaf\xb8\xe5\xbf\x85\xe9\xa1\xbb\xe4\xb8\xba1920*600, \xe5\x90\xa6\xe5\x88\x99\xe5\xbd\xb1\xe5\x93\x8d\xe6\x92\xad\xe6\x94\xbe\xe6\x95\x88\xe6\x9e\x9c', upload_to=b'index/slide/', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'db_table': 'slide',
                'verbose_name': '\u9996\u9875\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad\u56fe',
            },
        ),
    ]
