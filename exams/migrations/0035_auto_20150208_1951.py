# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0034_auto_20150208_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participantresult',
            old_name='participant',
            new_name='user',
        ),
    ]
