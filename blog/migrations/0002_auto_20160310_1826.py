# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(upload_to=b'blog/', null=True, verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5206\u7c7b', to='blog.BlogType', help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*'),
        ),
        migrations.AlterField(
            model_name='blogbigtype',
            name='name',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=50, verbose_name=b'\xe5\xa4\xa7\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='bigtype',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5927\u5206\u7c7b', to='blog.BlogBigType', help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*'),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='name',
            field=models.CharField(help_text=b'*\xe5\xbf\x85\xe5\xa1\xab*', max_length=50, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d'),
        ),
    ]
