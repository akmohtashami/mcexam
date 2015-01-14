# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20150114_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(help_text='\u0633\u0648\u0627\u0644\u0627\u062a \u0628\u0631\u0627\u0633\u0627\u0633 \u0634\u0645\u0627\u0631\u0647 \u0634\u0627\u0646 \u0645\u0631\u062a\u0628 \u0648 \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0645\u06cc \u0634\u0648\u0646\u062f', verbose_name='\u0634\u0645\u0627\u0631\u0647 \u06cc \u0633\u0648\u0627\u0644'),
            preserve_default=True,
        ),
    ]
