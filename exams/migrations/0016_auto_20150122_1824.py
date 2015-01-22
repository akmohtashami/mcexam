# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0015_auto_20150121_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': '\u0622\u0632\u0645\u0648\u0646', 'verbose_name_plural': '\u0622\u0632\u0645\u0648\u0646 \u0647\u0627', 'permissions': (('can_view', '\u062a\u0648\u0627\u0646\u0627\u06cc\u06cc \u062f\u06cc\u062f\u0646 \u0622\u0632\u0645\u0648\u0646 \u0647\u0627 \u0631\u0627 \u062f\u0627\u0631\u062f'), ('can_import_answer', '\u0627\u062c\u0627\u0632\u0647 \u06cc \u0648\u0627\u0631\u062f \u06a9\u0631\u062f\u0646 \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u062f\u0627\u0631\u062f'))},
        ),
    ]
