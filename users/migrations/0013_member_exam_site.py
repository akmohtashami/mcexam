# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0014_auto_20150120_2055'),
        ('users', '0012_auto_20150121_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='exam_site',
            field=models.ForeignKey(blank=True, to='exams.ExamSite', null=True),
            preserve_default=True,
        ),
    ]
