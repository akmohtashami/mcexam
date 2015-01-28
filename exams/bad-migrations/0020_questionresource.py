# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import exams.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0018_exam_exam_pdf_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/'), upload_to=exams.models.exam_based_file_path)),
                ('exam', models.ForeignKey(verbose_name='\u0622\u0632\u0645\u0648\u0646', to='exams.Exam')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
