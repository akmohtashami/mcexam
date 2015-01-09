# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150105_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '\u06a9\u0627\u0631\u0628\u0631', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is user activated'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Is administrator'),
            preserve_default=True,
        ),
    ]
