# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_auto_20150120_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Position'),
            preserve_default=True,
        ),
    ]
