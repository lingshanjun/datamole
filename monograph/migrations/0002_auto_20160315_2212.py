# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monograph', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonoChapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(help_text=b"*\xe5\xbf\x85\xe5\xa1\xab*, \xe4\xb8\xba\xe6\x95\xb4\xe6\x95\xb0, \xe5\xa6\x82'0','1','2'\xe7\xad\x89", verbose_name=b'\xe7\xab\xa0\xe5\xba\x8f\xe5\x8f\xb7')),
                ('title', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=100, verbose_name=b'\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('list', models.ForeignKey(verbose_name='\u6240\u5c5e\u4e13\u8457', to='monograph.MonoList', help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*')),
            ],
            options={
                'db_table': 'monograph_chapter',
                'verbose_name': '\u4e13\u8457\u7ae0\u5217\u8868',
                'verbose_name_plural': '\u4e13\u8457\u7ae0\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='MonoSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.FloatField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe5\x8f\xaa\xe6\x94\xaf\xe6\x8c\x81\xe4\xba\x8c\xe7\xba\xa7\xe6\xa0\x87\xe9\xa2\x98\xe7\x9a\x84\xe5\xba\x8f\xe5\x8f\xb7\xef\xbc\x8c\xe5\xa6\x821.1\xef\xbc\x8c2.3\xef\xbc\x8c\xe4\xb8\x8d\xe6\x94\xaf\xe6\x8c\x81\xe5\x85\xb6\xe5\xae\x83\xe7\xba\xa7\xe6\xa0\x87\xe9\xa2\x98\xef\xbc\x8c\xe5\xa6\x821.1.2\xef\xbc\x8c3.4.2.1\xe7\xad\x89', verbose_name=b'\xe8\x8a\x82\xe5\xba\x8f\xe5\x8f\xb7')),
                ('title', models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=100, verbose_name=b'\xe8\x8a\x82\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(help_text=b'\xe5\x8f\xaf\xe5\x9c\xa8\xe6\xad\xa4\xe5\xa4\x84\xe7\xbc\x96\xe8\xbe\x91\xe6\xaf\x8f\xe7\xab\xa0\xe7\x9a\x84\xe5\x85\xb7\xe4\xbd\x93\xe5\x86\x85\xe5\xae\xb9,\xe6\xb3\xa8\xe6\x84\x8f:', verbose_name=b'\xe5\x85\xb7\xe4\xbd\x93\xe5\x86\x85\xe5\xae\xb9')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('chapter', models.ForeignKey(verbose_name='\u6240\u5c5e\u7ae0\u76ee\u5f55', to='monograph.MonoChapter', help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*')),
            ],
            options={
                'db_table': 'monograph_section',
                'verbose_name': '\u4e13\u8457\u8282\u5217\u8868',
                'verbose_name_plural': '\u4e13\u8457\u8282\u5217\u8868',
            },
        ),
        migrations.AlterField(
            model_name='monobuy',
            name='link',
            field=models.URLField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='monobuy',
            name='priority',
            field=models.SmallIntegerField(default=0, help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe4\xbb\x8e0\xe5\xbc\x80\xe5\xa7\x8b\xe7\x9a\x84\xe6\x95\xb4\xe6\x95\xb0,\xe7\x94\xa8\xe4\xba\x8e\xe8\xae\xbe\xe7\xbd\xae\xe9\x93\xbe\xe6\x8e\xa5\xe7\x9a\x84\xe9\xa1\xba\xe5\xba\x8f,\xe6\x95\xb0\xe8\xb6\x8a\xe5\xa4\xa7,\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7\xe8\xb6\x8a\xe9\xab\x98,\xe9\xbb\x98\xe8\xae\xa4\xe4\xb8\xba0', verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='monocover',
            name='priority',
            field=models.SmallIntegerField(default=0, help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe4\xbb\x8e0\xe5\xbc\x80\xe5\xa7\x8b\xe7\x9a\x84\xe6\x95\xb4\xe6\x95\xb0,\xe7\x94\xa8\xe4\xba\x8e\xe8\xae\xbe\xe7\xbd\xae\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe7\x9a\x84\xe9\xa1\xba\xe5\xba\x8f,\xe6\x95\xb0\xe8\xb6\x8a\xe5\xa4\xa7,\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7\xe8\xb6\x8a\xe9\xab\x98,\xe9\xbb\x98\xe8\xae\xa4\xe4\xb8\xba0', verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7'),
        ),
    ]
