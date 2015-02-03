# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0022_question_is_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InfoBox',
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_info',
        ),
    ]
