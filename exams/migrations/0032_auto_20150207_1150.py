# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0031_auto_20150205_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_score',
            field=models.PositiveSmallIntegerField(default=4, help_text='Amount of score which is increased for correct answer', verbose_name='Correct Score'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='wrong_score',
            field=models.PositiveSmallIntegerField(default=1, help_text='Amount of score which is decreased for incorrent answer', verbose_name='Wrong Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='activation_date',
            field=models.DateTimeField(help_text='\u067e\u0633 \u0627\u0632 \u0627\u06cc\u0646 \u0632\u0645\u0627\u0646\u060c \u0622\u0632\u0645\u0648\u0646 \u0628\u0627\u0632 \u0645\u062d\u0633\u0648\u0628 \u0645\u06cc \u0634\u0648\u062f. \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f\u0647 \u0647\u0627(\u0645\u0633\u0626\u0648\u0644\u06cc\u0646) \u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u0633\u0648\u0627\u0644\u0627\u062a \u0631\u0627 \u062f\u0631\u06cc\u0627\u0641\u062a \u06a9\u0646\u0646\u062f \u0648 \u067e\u0627\u0633\u062e \u0628\u0631\u06af \u0647\u0627 \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f. \u0647\u0645\u0647 \u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u067e\u0627\u0633\u062e \u0628\u0631\u06af \u062e\u0648\u062f \u0631\u0627 \u0628\u0628\u06cc\u0646\u0646\u062f', verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0641\u0639\u0627\u0644 \u0633\u0627\u0632\u06cc'),
            preserve_default=True,
        ),
    ]
