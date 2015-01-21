# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_auto_20150120_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': '\u0622\u0632\u0645\u0648\u0646', 'verbose_name_plural': '\u0622\u0632\u0645\u0648\u0646 \u0647\u0627', 'permissions': (('can_view', 'Can view exam'), ('can_import_answer', 'Can import answer sheets'))},
        ),
        migrations.RenameField(
            model_name='examsite',
            old_name='manager',
            new_name='importer',
        ),
    ]
