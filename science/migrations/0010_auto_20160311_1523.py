# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0009_auto_20160311_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='status',
            field=models.SmallIntegerField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(3, b'\xe6\x8e\x88\xe6\x9d\x83'), (1, b'\xe7\x94\xb3\xe8\xaf\xb7'), (2, b'\xe5\x85\xac\xe5\xbc\x80')]),
        ),
    ]
