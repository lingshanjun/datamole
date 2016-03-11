# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160310_1826'),
        ('science', '0010_auto_20160311_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=50, verbose_name=b'\xe8\xbd\xaf\xe8\x91\x97\xe5\x90\x8d\xe7\xa7\xb0')),
                ('descripe', models.TextField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe8\xbd\xaf\xe8\x91\x97\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('all_creators', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe8\xaf\xb7\xe6\x8c\x89\xe9\xa1\xba\xe5\xba\x8f\xe8\xbe\x93\xe5\x85\xa5\xe6\x89\x80\xe6\x9c\x89\xe5\x8f\x91\xe6\x98\x8e\xe4\xba\xba\xe7\xac\x94\xe5\x90\x8d\xef\xbc\x8c\xe5\xa6\x82\xe2\x80\x9c\xe5\xbc\xa0\xe4\xb8\x89\xef\xbc\x8c\xe6\x9d\x8e\xe5\x9b\x9b\xef\xbc\x8c\xe7\x8e\x8b\xe4\xba\x94\xe2\x80\x9d', max_length=50, verbose_name=b'\xe6\x89\x80\xe6\x9c\x89\xe5\x8f\x91\xe6\x98\x8e\xe4\xba\xba')),
                ('number', models.CharField(max_length=50, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
                ('time', models.DateField(verbose_name=b'\xe9\xa6\x96\xe6\xac\xa1\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('pic', models.ImageField(upload_to=b'soft/pic/', verbose_name=b'\xe8\xaf\x81\xe4\xb9\xa6\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('creators', models.ManyToManyField(help_text=b'\xe5\x9c\xa8\xe5\x88\x97\xe8\xa1\xa8\xe4\xb8\xad\xe9\x80\x89\xe6\x8b\xa9\xe5\x8c\x85\xe5\x90\xab\xe7\x9a\x84\xe5\x8f\x91\xe6\x98\x8e\xe4\xba\xba', to='member.Member', verbose_name='\u53d1\u660e\u4eba')),
            ],
            options={
                'db_table': 'soft',
                'verbose_name': '\u8f6f\u8457',
                'verbose_name_plural': '\u8f6f\u8457',
            },
        ),
        migrations.AlterField(
            model_name='patent',
            name='descripe',
            field=models.TextField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe4\xb8\x93\xe5\x88\xa9\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
    ]
