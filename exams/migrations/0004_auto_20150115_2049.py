# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20150114_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='statement',
            field=models.TextField(verbose_name='\u0635\u0648\u0631\u062a \u0633\u0648\u0627\u0644'),
            preserve_default=True,
        ),
    ]
