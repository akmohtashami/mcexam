# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20150115_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='question_per_column',
            field=models.PositiveIntegerField(default=20, verbose_name='Number of questions per column in answer sheet'),
            preserve_default=True,
        ),
    ]
