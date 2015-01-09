# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20150107_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='end_date',
            field=models.DateTimeField(verbose_name='End Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_date',
            field=models.DateTimeField(verbose_name='Start Date'),
            preserve_default=True,
        ),
    ]
