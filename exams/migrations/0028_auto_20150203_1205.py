# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0027_auto_20150203_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='show_results',
        ),
        migrations.AddField(
            model_name='exam',
            name='publish_results_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0), help_text='After this time the results and correct answers will be published ', verbose_name='Result publishing date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='activation_date',
            field=models.DateTimeField(default=datetime.datetime(2013, 1, 1, 0, 0), help_text='After this time the exam is considered open. Importers can download the questions and import answer sheets. Everybody can see their answer sheet.', verbose_name='Activation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='sealing_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 1, 1, 0, 0), help_text='After this time the exam is sealed. Importers will no longer be able to import answer sheets', verbose_name='Sealing date'),
            preserve_default=True,
        ),
    ]
