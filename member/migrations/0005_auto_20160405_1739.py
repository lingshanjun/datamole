# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20160405_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5'),
        ),
    ]
