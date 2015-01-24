# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0016_auto_20150122_1824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examsite',
            options={'verbose_name': '\u0645\u06a9\u0627\u0646 \u0628\u0631\u06af\u0632\u0627\u0631\u06cc', 'verbose_name_plural': '\u0645\u06a9\u0627\u0646 \u0647\u0627\u06cc \u0628\u0631\u06af\u0632\u0627\u0631\u06cc'},
        ),
        migrations.AlterField(
            model_name='examsite',
            name='exam',
            field=models.ForeignKey(verbose_name='\u0622\u0632\u0645\u0648\u0646', to='exams.Exam'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examsite',
            name='importer',
            field=models.ForeignKey(verbose_name='\u0648\u0627\u0631\u062f \u06a9\u0646\u0646\u062f\u0647', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examsite',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0645\u06a9\u0627\u0646 \u0628\u0631\u06af\u0632\u0627\u0631\u06cc'),
            preserve_default=True,
        ),
    ]
