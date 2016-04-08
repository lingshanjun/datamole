# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20160405_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='introduction',
            field=models.TextField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe8\xaf\xa6\xe7\xbb\x86\xe4\xbb\x8b\xe7\xbb\x8d\xe6\x88\x90\xe5\x91\x98\xe7\x9a\x84\xe6\x83\x85\xe5\x86\xb5,\xe5\xa4\x9a\xe5\xa4\x9a\xe7\x9b\x8a\xe5\x96\x84', null=True, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='member',
            name='descripe',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*, \xe7\xb1\xbb\xe4\xbc\xbc\xe4\xba\x8e\xe5\xba\xa7\xe5\x8f\xb3\xe9\x93\xad', max_length=100, verbose_name=b'\xe4\xb8\x80\xe5\x8f\xa5\xe8\xaf\x9d\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
    ]
