# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160310_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', upload_to=b'team/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='descripe',
            field=models.TextField(default=b'\xe4\xb8\x80\xe5\x8f\xa5\xe8\xaf\x9d\xe4\xbb\x8b\xe7\xbb\x8d\xe8\x87\xaa\xe5\xb7\xb1', help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='member',
            name='jionin',
            field=models.DateField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe5\x8a\xa0\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=10, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='member',
            name='search',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=100, verbose_name=b'\xe7\xa0\x94\xe7\xa9\xb6\xe6\x96\xb9\xe5\x90\x91'),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.SmallIntegerField(default=0, help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe4\xbf\x9d\xe5\xaf\x86'), (1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='work_status',
            field=models.SmallIntegerField(default=1, help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe5\x9c\xa8\xe8\x81\x8c\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe7\xa6\xbb\xe8\x81\x8c'), (1, b'\xe5\x9c\xa8\xe8\x81\x8c')]),
        ),
    ]
