# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0013_auto_20150120_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='question_per_column',
            new_name='questions_per_column',
        ),
    ]
