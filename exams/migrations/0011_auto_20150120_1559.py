# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminsortable.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0010_auto_20150120_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Exam Site')),
                ('exam', models.ForeignKey(to='exams.Exam')),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
