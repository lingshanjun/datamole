# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20160408_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='jionin',
            new_name='joinin',
        ),
    ]
