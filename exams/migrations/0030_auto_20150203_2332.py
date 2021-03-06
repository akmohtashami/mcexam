# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0029_auto_20150203_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='activation_date',
            field=models.DateTimeField(help_text='\u067e\u0633 \u0627\u0632 \u0627\u06cc\u0646 \u0632\u0645\u0627\u0646\u060c \u0622\u0632\u0645\u0648\u0646 \u0628\u0627\u0632 \u0645\u062d\u0633\u0648\u0628 \u0645\u06cc \u0634\u0648\u062f. \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f\u0647 \u0647\u0627(\u0645\u0633\u0626\u0648\u0644\u06cc\u0646) \u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u0633\u0648\u0627\u0644\u0627\u062a \u0631\u0627 \u062f\u0631\u06cc\u0627\u0641\u062a \u06a9\u0646\u0646\u062f \u0648 \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u0647\u0627 \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f. \u0647\u0645\u0647 \u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u06cc \u062e\u0648\u062f \u0631\u0627 \u0628\u0628\u06cc\u0646\u0646\u062f', verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0641\u0639\u0627\u0644 \u0633\u0627\u0632\u06cc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='publish_results_date',
            field=models.DateTimeField(help_text='\u067e\u0633 \u0627\u0632 \u0627\u06cc\u0646 \u0632\u0645\u0627\u0646 \u0646\u062a\u0627\u06cc\u062c \u0648 \u067e\u0627\u0633\u062e \u0647\u0627\u06cc \u0635\u062d\u06cc\u062d \u0645\u0646\u062a\u0634\u0631 \u0645\u06cc \u0634\u0648\u0646\u062f', verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0627\u0646\u062a\u0634\u0627\u0631 \u0646\u062a\u0627\u06cc\u062c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='sealing_date',
            field=models.DateTimeField(help_text='\u067e\u0633 \u0627\u0632 \u0627\u06cc\u0646 \u0632\u0645\u0627\u0646 \u0622\u0632\u0645\u0648\u0646 \u0645\u0647\u0631 \u0648 \u0645\u0648\u0645 \u0645\u06cc \u0634\u0648\u062f. \u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f\u0647 \u0647\u0627 \u062f\u06cc\u06af\u0631 \u0646\u0645\u06cc \u062a\u0648\u0627\u0646\u0646\u062f \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u0647\u0627 \u0631\u0627 \u0627\u0636\u0627\u0641\u0647 \u06cc\u0627 \u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0646\u0646\u062f', verbose_name='\u0632\u0645\u0627\u0646 \u0645\u0647\u0631 \u0648 \u0645\u0648\u0645 \u0634\u062f\u0646 \u0622\u0632\u0645\u0648\u0646'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='is_info',
            field=models.BooleanField(default=False, help_text='\u0627\u06af\u0631 \u0645\u06cc \u062e\u0648\u0627\u0647\u06cc\u062f \u0627\u0637\u0644\u0627\u0639\u0627\u062a\u06cc \u0628\u06cc\u0646 \u0628\u0631\u062e\u06cc \u0627\u0632 \u0633\u0648\u0627\u0644\u0627\u062a \u0642\u0631\u0627\u0631 \u062f\u0647\u06cc\u062f\u060c \u0645\u062a\u0646 \u0631\u0627 \u062f\u0631\u0648\u0646 \u0635\u0648\u0631\u062a \u0633\u0648\u0627\u0644 \u0628\u0646\u0648\u06cc\u0633\u06cc\u062f \u0648 \u0627\u06cc\u0646 \u06af\u0632\u06cc\u0646\u0647 \u0631\u0627 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f.', verbose_name='\u0627\u0637\u0644\u0627\u0639\u0627\u062a'),
            preserve_default=True,
        ),
    ]
