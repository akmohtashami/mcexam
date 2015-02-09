# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0042_auto_20150209_1858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='madechoice',
            options={'ordering': ['user', 'choice__question__exam', 'choice__question'], 'verbose_name': 'Made Choice'},
        ),
        migrations.AlterModelOptions(
            name='participantresult',
            options={'ordering': ['exam', '-score'], 'verbose_name': 'Participant Result', 'verbose_name_plural': 'Participants Results'},
        ),
    ]
