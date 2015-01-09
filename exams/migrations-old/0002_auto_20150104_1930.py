# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='end_date',
            field=django_jalali.db.models.jDateTimeField(verbose_name=b'End Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_date',
            field=django_jalali.db.models.jDateTimeField(verbose_name=b'Start Date'),
            preserve_default=True,
        ),
    ]
