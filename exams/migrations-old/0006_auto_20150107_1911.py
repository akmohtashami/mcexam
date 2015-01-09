# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20150107_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='order',
            field=models.IntegerField(default=0, unique=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(unique=True, auto_created=True),
            preserve_default=True,
        ),
    ]
