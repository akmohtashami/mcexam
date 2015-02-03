# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0024_exam_statement_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='statement_file',
            new_name='statements_file',
        ),
    ]
