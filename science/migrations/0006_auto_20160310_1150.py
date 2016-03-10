# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0005_auto_20160310_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.URLField(help_text=b'\xe4\xbe\x8b\xe5\xa6\x82 https://www.baidu.com/', verbose_name=b'\xe5\x85\xac\xe5\xbc\x80\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
    ]
