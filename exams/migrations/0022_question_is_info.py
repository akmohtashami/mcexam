# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0021_auto_20150202_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_info',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
    ]
