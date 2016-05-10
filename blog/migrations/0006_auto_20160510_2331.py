# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_authos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='authos',
            new_name='authors',
        ),
    ]
