# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20150128_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='filename',
            field=models.CharField(max_length=1000, verbose_name='\u0646\u0627\u0645 \u0641\u0627\u06cc\u0644', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='is_private',
            field=models.BooleanField(default=True, help_text='\u0645\u0646\u0627\u0628\u0639 \u062e\u0635\u0648\u0635\u06cc \u062a\u0648\u0633\u0637 \u0648\u0628 \u0633\u0631\u0648\u0631 \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0646\u0645\u06cc \u0634\u0648\u0646\u062f', verbose_name='\u062e\u0635\u0648\u0635\u06cc'),
            preserve_default=True,
        ),
    ]
