# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20150128_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': 'Resource', 'verbose_name_plural': 'Resources'},
        ),
    ]
