# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20150107_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=10000)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(to='exams.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choices',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]
