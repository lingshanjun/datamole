# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160909_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='abstract',
            field=models.TextField(help_text='*\u5fc5\u586b*', null=True, verbose_name='\u7b80\u4ecb'),
        ),
    ]
