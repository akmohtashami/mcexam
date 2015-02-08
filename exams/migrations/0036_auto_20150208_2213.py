# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0035_auto_20150208_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='madechoice',
            options={'ordering': ['user', 'choice__question__exam', 'choice__question']},
        ),
    ]
