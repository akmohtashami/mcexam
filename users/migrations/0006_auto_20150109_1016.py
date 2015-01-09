# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150107_0228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='member',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='A superuser has all permissions without explicitly assigning them', verbose_name='Superuser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
            preserve_default=True,
        ),
    ]
