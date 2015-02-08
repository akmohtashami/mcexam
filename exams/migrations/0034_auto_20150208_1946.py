# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0033_participantresult'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participantresult',
            options={'ordering': ['exam', '-score']},
        ),
    ]
