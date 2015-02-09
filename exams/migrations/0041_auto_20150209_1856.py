# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0040_auto_20150209_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': '\u0622\u0632\u0645\u0648\u0646', 'verbose_name_plural': '\u0622\u0632\u0645\u0648\u0646 \u0647\u0627', 'permissions': (('can_view', '\u062a\u0648\u0627\u0646\u0627\u06cc\u06cc \u062f\u06cc\u062f\u0646 \u0622\u0632\u0645\u0648\u0646 \u0647\u0627 \u0631\u0627 \u062f\u0627\u0631\u062f'), ('can_import', '\u0627\u062c\u0627\u0632\u0647 \u06cc \u0648\u0627\u0631\u062f \u06a9\u0631\u062f\u0646 \u067e\u0627\u0633\u062e \u0628\u0631\u06af \u062f\u0627\u0631\u062f'), ('out_of_competition', '\u0628\u0647 \u0635\u0648\u0631\u062a \u063a\u06cc\u0631\u0631\u0633\u0645\u06cc \u0634\u0631\u06a9\u062a \u06a9\u0631\u062f\u0647'), ('moderate_imports', 'Has access to all exam sites. Import access must be given separately'), ('see_all_results', 'Can see all results'))},
        ),
    ]
