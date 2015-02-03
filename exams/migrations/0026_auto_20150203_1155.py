# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import exams.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0025_auto_20150203_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='activation_date',
            field=models.DateTimeField(default=datetime.datetime(2013, 1, 1, 0, 0), help_text='After this time the exam is considered open. Importers can download the questions and import answer sheets Everybody else can see their answer sheet', verbose_name='Activation date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exam',
            name='sealing_date',
            field=models.DateTimeField(default=datetime.datetime(2013, 1, 1, 0, 0), help_text='After this time the exam is sealed. Importers will no longer be able to import answer sheets', verbose_name='Sealing date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exam',
            name='show_results',
            field=models.BooleanField(default=False, help_text='If checked, participants can see their results. Also importers can download results of their participantsBe advised to use this only after sealing date since this will publish actual results as well', verbose_name='Show results'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='end_date',
            field=models.DateTimeField(verbose_name='Online exam end date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_date',
            field=models.DateTimeField(verbose_name='Online exam start date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='statements_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/'), max_length=5000, null=True, upload_to=exams.models.get_statement_path, blank=True),
            preserve_default=True,
        ),
    ]
