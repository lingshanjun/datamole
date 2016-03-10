# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160310_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae')),
                ('abstract', models.TextField(verbose_name=b'\xe6\x91\x98\xe8\xa6\x81')),
                ('all_authors', models.CharField(help_text=b'\xe8\xaf\xb7\xe6\x8c\x89\xe9\xa1\xba\xe5\xba\x8f\xe8\xbe\x93\xe5\x85\xa5\xe6\x89\x80\xe6\x9c\x89\xe4\xbd\x9c\xe8\x80\x85\xe7\xac\x94\xe5\x90\x8d\xef\xbc\x8c\xe5\xa6\x82\xe2\x80\x9c\xe5\xbc\xa0\xe4\xb8\x89\xef\xbc\x8c\xe6\x9d\x8e\xe5\x9b\x9b\xef\xbc\x8c\xe7\x8e\x8b\xe4\xba\x94\xe2\x80\x9d', max_length=50, verbose_name=b'\xe6\x89\x80\xe6\x9c\x89\xe4\xbd\x9c\xe8\x80\x85')),
                ('pub_time', models.DateField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('pub_location', models.CharField(max_length=50, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe5\x9c\xb0\xe7\x82\xb9', blank=True)),
                ('pub_pulications', models.CharField(max_length=50, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe5\x88\x8a\xe7\x89\xa9', blank=True)),
                ('link', models.URLField(verbose_name=b'\xe5\x85\xac\xe5\xbc\x80\xe9\x93\xbe\xe6\x8e\xa5')),
                ('is_download', models.BooleanField(default=False, verbose_name=b'\xe5\x85\x81\xe8\xae\xb8\xe4\xb8\x8b\xe8\xbd\xbd')),
                ('dl_file', models.FileField(upload_to=b'paper/download/', verbose_name=b'\xe4\xbe\x9b\xe4\xb8\x8b\xe8\xbd\xbd\xe7\x9a\x84\xe6\x96\x87\xe4\xbb\xb6', blank=True)),
                ('authors', models.ManyToManyField(help_text=b'\xe5\x9c\xa8\xe5\x88\x97\xe8\xa1\xa8\xe4\xb8\xad\xe9\x80\x89\xe6\x8b\xa9\xe5\x8c\x85\xe5\x90\xab\xe7\x9a\x84\xe4\xbd\x9c\xe8\x80\x85', to='member.Member', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
            ],
            options={
                'db_table': 'paper',
                'verbose_name': '\u8bba\u6587',
                'verbose_name_plural': '\u8bba\u6587',
            },
        ),
    ]
