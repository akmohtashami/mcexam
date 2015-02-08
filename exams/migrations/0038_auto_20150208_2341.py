# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0037_auto_20150208_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantresult',
            name='correct',
            field=models.PositiveIntegerField(verbose_name='\u067e\u0627\u0633\u062e \u0647\u0627\u06cc \u0635\u062d\u06cc\u062d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participantresult',
            name='score',
            field=models.PositiveIntegerField(verbose_name='Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participantresult',
            name='user',
            field=models.ForeignKey(verbose_name='\u0634\u0631\u06a9\u062a \u06a9\u0646\u0646\u062f\u0647', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participantresult',
            name='wrong',
            field=models.PositiveIntegerField(verbose_name='\u067e\u0627\u0633\u062e \u0647\u0627\u06cc \u063a\u0644\u0637'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_score',
            field=models.PositiveSmallIntegerField(default=4, help_text='\u0645\u06cc\u0632\u0627\u0646 \u0646\u0645\u0631\u0647 \u0627\u06cc \u06a9\u0647 \u0628\u0647 \u0627\u0632\u0627\u06cc \u067e\u0627\u0633\u062e \u062f\u0631\u0633\u062a \u0627\u0636\u0627\u0641\u0647 \u0645\u06cc \u0634\u0648\u062f', verbose_name='\u0627\u0645\u062a\u06cc\u0627\u0632 \u067e\u0627\u0633\u062e \u0635\u062d\u06cc\u062d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='wrong_penalty',
            field=models.PositiveSmallIntegerField(default=1, help_text='\u0645\u06cc\u0632\u0627\u0646 \u0646\u0645\u0631\u0647 \u0627\u06cc \u06a9\u0647 \u0628\u0647 \u0627\u0632\u0627\u06cc \u067e\u0627\u0633\u062e \u063a\u0644\u0637 \u06a9\u0645 \u0645\u06cc \u0634\u0648\u062f', verbose_name='\u062c\u0631\u06cc\u0645\u0647 \u06cc \u067e\u0627\u0633\u062e \u063a\u0644\u0637'),
            preserve_default=True,
        ),
    ]
