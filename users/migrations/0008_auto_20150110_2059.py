# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150109_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '\u06a9\u0627\u0631\u0628\u0631', 'verbose_name_plural': '\u06a9\u0627\u0631\u0628\u0631\u0627\u0646'},
        ),
        migrations.AddField(
            model_name='member',
            name='grade',
            field=models.CharField(max_length=6, null=True, verbose_name='Grade', choices=[(b'before', 'Before High School'), (b'first', 'First Grade'), (b'second', 'Second Grade'), (b'third', 'Third Grade'), (b'past', 'After Third Grade')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='school',
            field=models.CharField(max_length=250, null=True, verbose_name='School'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(unique=True, max_length=250, verbose_name='\u067e\u0633\u062a \u0627\u0644\u06a9\u062a\u0631\u0648\u0646\u06cc\u06a9\u06cc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='\u0646\u0627\u0645(\u0628\u0647 \u0641\u0627\u0631\u0633\u06cc)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name_en',
            field=models.CharField(max_length=250, verbose_name='\u0646\u0627\u0645(\u0628\u0647 \u0627\u0646\u06af\u0644\u06cc\u0633\u06cc)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u0641\u0639\u0627\u0644'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=250, verbose_name='\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc(\u0628\u0647 \u0641\u0627\u0631\u0633\u06cc)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name_en',
            field=models.CharField(max_length=250, verbose_name='\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc(\u0628\u0647 \u0627\u0646\u06af\u0644\u06cc\u0633\u06cc)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(unique=True, max_length=250, verbose_name='\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc'),
            preserve_default=True,
        ),
    ]
