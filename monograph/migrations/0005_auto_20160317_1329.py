# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monograph', '0004_auto_20160315_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monosection',
            name='content',
        ),
        migrations.AddField(
            model_name='monochapter',
            name='mono_chapter_content',
            field=models.TextField(help_text=b'\xe5\x8f\xaf\xe5\x9c\xa8\xe6\xad\xa4\xe5\xa4\x84\xe7\xbc\x96\xe8\xbe\x91\xe6\x9c\xac\xe7\xab\xa0\xe7\x9a\x84\xe4\xbb\x8b\xe7\xbb\x8d\xe5\x86\x85\xe5\xae\xb9', verbose_name=b'\xe6\x9c\xac\xe7\xab\xa0\xe4\xbb\x8b\xe7\xbb\x8d', blank=True),
        ),
        migrations.AddField(
            model_name='monosection',
            name='mono_section_content',
            field=models.TextField(help_text=b'\xe5\x8f\xaf\xe5\x9c\xa8\xe6\xad\xa4\xe5\xa4\x84\xe7\xbc\x96\xe8\xbe\x91\xe6\xaf\x8f\xe7\xab\xa0\xe7\x9a\x84\xe5\x85\xb7\xe4\xbd\x93\xe5\x86\x85\xe5\xae\xb9,\xe6\xb3\xa8\xe6\x84\x8f:', verbose_name=b'\xe5\x85\xb7\xe4\xbd\x93\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
    ]
