# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20150120_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='order',
            field=models.PositiveIntegerField(unique=True, verbose_name='Position'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(verbose_name=b'Related question', to='exams.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(verbose_name='\u0622\u0632\u0645\u0648\u0646 \u0645\u0631\u0628\u0648\u0637\u0647', to='exams.Exam'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(unique=True, verbose_name='Position'),
            preserve_default=True,
        ),
    ]
