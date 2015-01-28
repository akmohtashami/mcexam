# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='is_private',
            field=models.BooleanField(default=True, help_text='Private resources are not served by webserver', verbose_name='Private'),
            preserve_default=True,
        ),
    ]
