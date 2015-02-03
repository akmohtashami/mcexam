# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0028_auto_20150203_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_info',
            field=models.BooleanField(default=False, help_text='If you want to put some info between some of the question write info in question statement and check this box', verbose_name='Info'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='activation_date',
            field=models.DateTimeField(default=datetime.datetime(2013, 1, 1, 0, 0), help_text='\u067e\u0633 \u0627\u0632 \u0627\u06cc\u0646 \u0632\u0645\u0627\u0646\u060c \u0622\u0632\u0645\u0648\u0646 \u0628\u0627\u0632 \u0645\u062d\u0633\u0648\u0628 \u0645\u06cc \u0634\u0648\u062f. \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f\u0647 \u0647\u0627(\u0645\u0633\u0626\u0648\u0644\u06cc\u0646) \u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u0633\u0648\u0627\u0644\u0627\u062a \u0631\u0627 \u062f\u0631\u06cc\u0627\u0641\u062a \u06a9\u0646\u0646\u062f \u0648 \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u0647\u0627 \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f. \u0647\u0645\u0647 \u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u06cc \u062e\u0648\u062f \u0631\u0627 \u0628\u0628\u06cc\u0646\u0646\u062f', verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0641\u0639\u0627\u0644 \u0633\u0627\u0632\u06cc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='online_end_date',
            field=models.DateTimeField(verbose_name='\u0632\u0645\u0627\u0646 \u067e\u0627\u06cc\u0627\u0646 \u0622\u0632\u0645\u0648\u0646 \u0622\u0646\u0644\u0627\u06cc\u0646'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='online_start_date',
            field=models.DateTimeField(verbose_name='\u0632\u0645\u0627\u0646 \u0634\u0631\u0648\u0639 \u0622\u0632\u0645\u0648\u0646 \u0622\u0646\u0644\u0627\u06cc\u0646'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='publish_results_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0), help_text='\u067e\u0633 \u0627\u0632 \u0627\u06cc\u0646 \u0632\u0645\u0627\u0646 \u0646\u062a\u0627\u06cc\u062c \u0648 \u067e\u0627\u0633\u062e \u0647\u0627\u06cc \u0635\u062d\u06cc\u062d \u0645\u0646\u062a\u0634\u0631 \u0645\u06cc \u0634\u0648\u0646\u062f', verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0627\u0646\u062a\u0634\u0627\u0631 \u0646\u062a\u0627\u06cc\u062c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='sealing_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 1, 1, 0, 0), help_text='\u067e\u0633 \u0627\u0632 \u0627\u06cc\u0646 \u0632\u0645\u0627\u0646 \u0622\u0632\u0645\u0648\u0646 \u0645\u0647\u0631 \u0648 \u0645\u0648\u0645 \u0645\u06cc \u0634\u0648\u062f. \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f\u0647 \u0647\u0627 \u062f\u06cc\u06af\u0631 \u0646\u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u0647\u0627 \u0631\u0627 \u0627\u0636\u0627\u0641\u0647 \u06cc\u0627 \u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0646\u0646\u062f', verbose_name='\u0632\u0645\u0627\u0646 \u0645\u0647\u0631 \u0648 \u0645\u0648\u0645 \u0634\u062f\u0646 \u0622\u0632\u0645\u0648\u0646'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(verbose_name='\u0622\u0632\u0645\u0648\u0646 \u0645\u0631\u0628\u0648\u0637\u0647', to='exams.Exam'),
            preserve_default=True,
        ),
    ]
