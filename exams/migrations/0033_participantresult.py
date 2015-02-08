# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0032_auto_20150207_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.PositiveIntegerField(verbose_name='Points')),
                ('correct', models.PositiveIntegerField(verbose_name='Correct answers')),
                ('wrong', models.PositiveIntegerField(verbose_name='Wrong answers')),
                ('rank', models.PositiveIntegerField(verbose_name='Rank')),
                ('exam', models.ForeignKey(verbose_name='\u0622\u0632\u0645\u0648\u0646', to='exams.Exam')),
                ('participant', models.ForeignKey(verbose_name='Participant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['exam', 'score'],
            },
            bases=(models.Model,),
        ),
    ]
