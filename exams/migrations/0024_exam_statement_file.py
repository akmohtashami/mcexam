# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import exams.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0023_auto_20150202_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='statement_file',
            field=models.FileField(max_length=5000, null=True, upload_to=exams.models.get_statement_path, blank=True),
            preserve_default=True,
        ),
    ]
