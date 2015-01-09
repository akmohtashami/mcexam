# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150105_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name='\u0627\u06cc\u0645\u06cc\u0644'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=1000, verbose_name='First Name (Native)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name_en',
            field=models.CharField(max_length=1000, verbose_name='(First Name (English)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is user activated?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Does user has administrative privileges?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=1000, verbose_name='Last Name (Native)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name_en',
            field=models.CharField(max_length=1000, verbose_name='Last Name (English)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(unique=True, max_length=200, verbose_name='\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc'),
            preserve_default=True,
        ),
    ]
