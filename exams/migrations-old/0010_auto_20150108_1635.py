# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_madechoice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'Exam', 'verbose_name_plural': 'Exams'},
        ),
        migrations.AlterField(
            model_name='question',
            name='statement',
            field=models.CharField(max_length=10000, verbose_name="Question's Statement"),
            preserve_default=True,
        ),
    ]
