# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('cover', models.CharField(max_length=500, null=True, verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe')),
                ('content_show', models.TextField(null=True, verbose_name=b'\xe6\xad\xa3\xe6\x96\x87\xe6\x98\xbe\xe7\xa4\xba')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('counts', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
                ('is_recomment', models.BooleanField(default=False, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90')),
                ('status', models.SmallIntegerField(default=0, verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\x8d\x89\xe7\xa8\xbf'), (1, b'\xe5\x8f\x91\xe5\xb8\x83')])),
            ],
            options={
                'db_table': 'blog_detail',
                'verbose_name': '\u535a\u5ba2\u8be6\u60c5',
                'verbose_name_plural': '\u535a\u5ba2\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='BlogBigType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\xa4\xa7\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'blog_bigtype',
                'verbose_name': '\u535a\u5ba2\u5927\u5206\u7c7b',
                'verbose_name_plural': '\u535a\u5ba2\u5927\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('bigtype', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xa4\xa7\xe5\x88\x86\xe7\xb1\xbb', to='blog.BlogBigType')),
            ],
            options={
                'db_table': 'blog_type',
                'verbose_name': '\u535a\u5ba2\u5206\u7c7b',
                'verbose_name_plural': '\u535a\u5ba2\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x88\x86\xe7\xb1\xbb', to='blog.BlogType'),
        ),
    ]
