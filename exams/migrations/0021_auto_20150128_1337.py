# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0020_auto_20150125_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionresource',
            name='exam',
        ),
        migrations.DeleteModel(
            name='QuestionResource',
        ),
    ]
