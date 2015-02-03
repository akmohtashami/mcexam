# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0020_auto_20150130_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoBox',
            fields=[
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'proxy': True,
            },
            bases=('exams.question',),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_pdf_template',
            field=models.TextField(default=b'', help_text='\u0642\u0627\u0644\u0628 \u062c\u0627\u0646\u06af\u0648-\u062a\u06a9 \u0628\u0631\u0627\u06cc \u0633\u0627\u062e\u062a \u0641\u0627\u06cc\u0644 \u0647\u0627\u06cc PDF', verbose_name='\u0642\u0627\u0644\u0628 PDF'),
            preserve_default=True,
        ),
    ]
