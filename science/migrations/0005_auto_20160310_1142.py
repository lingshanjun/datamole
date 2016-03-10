# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0004_auto_20160310_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(help_text=b'\xe5\x9c\xa8\xe5\x88\x97\xe8\xa1\xa8\xe4\xb8\xad\xe9\x80\x89\xe6\x8b\xa9\xe5\x8c\x85\xe5\x90\xab\xe7\x9a\x84\xe4\xbd\x9c\xe8\x80\x85', to='member.Member', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', blank=True),
        ),
    ]
