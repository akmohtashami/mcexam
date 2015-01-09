# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20150107_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='choice',
            name='order',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
