# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0036_auto_20150208_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='wrong_score',
        ),
        migrations.AddField(
            model_name='question',
            name='wrong_penalty',
            field=models.PositiveSmallIntegerField(default=1, help_text='Amount of score which is decreased for incorrent answer', verbose_name='Wrong Answer Penalty'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_score',
            field=models.PositiveSmallIntegerField(default=4, help_text='Amount of score which is increased for correct answer', verbose_name='Correct Answer Score'),
            preserve_default=True,
        ),
    ]
