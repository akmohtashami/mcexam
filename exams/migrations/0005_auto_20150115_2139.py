# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminsortable.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20150115_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=adminsortable.fields.SortableForeignKey(verbose_name=b'Related question', to='exams.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=adminsortable.fields.SortableForeignKey(verbose_name='\u0622\u0632\u0645\u0648\u0646 \u0645\u0631\u0628\u0648\u0637\u0647', to='exams.Exam'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=True,
        ),
    ]
