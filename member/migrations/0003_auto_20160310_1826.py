# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160310_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(upload_to=b'team/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
        ),
    ]
