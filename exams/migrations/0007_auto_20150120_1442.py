# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_exam_question_per_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='question_per_column',
            field=models.PositiveIntegerField(default=20, verbose_name='\u062a\u0639\u062f\u0627\u062f \u0633\u0648\u0627\u0644\u0627\u062a \u062f\u0631 \u0647\u0631 \u0633\u062a\u0648\u0646 \u067e\u0627\u0633\u062e\u0646\u0627\u0645\u0647'),
            preserve_default=True,
        ),
    ]
