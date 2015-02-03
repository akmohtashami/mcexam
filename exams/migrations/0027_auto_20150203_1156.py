# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0026_auto_20150203_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='end_date',
            new_name='online_end_date',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='start_date',
            new_name='online_start_date',
        ),
    ]
