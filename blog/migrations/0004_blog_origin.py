# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160408_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='origin',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8e\x9f\xe5\x88\x9b', choices=[(0, b'\xe5\x8e\x9f\xe5\x88\x9b'), (1, b'\xe8\xbd\xac\xe8\xbd\xbd')]),
        ),
    ]
