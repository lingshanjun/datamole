# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monograph', '0003_auto_20160315_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monochapter',
            name='order',
            field=models.SmallIntegerField(help_text=b"*\xe5\xbf\x85\xe5\xa1\xab*, \xe4\xb8\xba\xe6\x95\xb4\xe6\x95\xb0,\xe4\xb8\xa5\xe6\xa0\xbc\xe5\xae\x89\xe8\xa3\x85\xe6\xad\xa4\xe6\xa0\xbc\xe5\xbc\x8f,'0','1','2'\xe7\xad\x89", verbose_name=b'\xe7\xab\xa0\xe5\xba\x8f\xe5\x8f\xb7'),
        ),
    ]
