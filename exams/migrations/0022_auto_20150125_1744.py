# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0021_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': '\u0622\u0632\u0645\u0648\u0646', 'verbose_name_plural': '\u0622\u0632\u0645\u0648\u0646 \u0647\u0627', 'permissions': (('can_view', '\u062a\u0648\u0627\u0646\u0627\u06cc\u06cc \u062f\u06cc\u062f\u0646 \u0622\u0632\u0645\u0648\u0646 \u0647\u0627 \u0631\u0627 \u062f\u0627\u0631\u062f'), ('can_import', '\u0627\u062c\u0627\u0632\u0647 \u06cc \u0648\u0627\u0631\u062f \u06a9\u0631\u062f\u0646 \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647 \u062f\u0627\u0631\u062f'))},
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_pdf_template',
            field=models.TextField(default=b'', help_text='\u0642\u0627\u0644\u0628 \u062c\u0627\u0646\u06af\u0648-\u062a\u06a9 \u0628\u0631\u0627\u06cc \u0633\u0627\u062e\u062a \u0641\u0627\u06cc\u0644 \u0647\u0627\u06cc PDF', verbose_name='\u0642\u0627\u0644\u0628 PDF'),
            preserve_default=True,
        ),
    ]
