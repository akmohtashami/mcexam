# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150110_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='grade',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='\u067e\u0627\u06cc\u0647', choices=[(b'before', '\u067e\u06cc\u0634 \u062f\u0628\u06cc\u0631\u0633\u062a\u0627\u0646\u06cc'), (b'first', '\u0627\u0648\u0644 \u062f\u0628\u06cc\u0631\u0633\u062a\u0627\u0646'), (b'second', '\u062f\u0648\u0645 \u062f\u0628\u06cc\u0631\u0633\u062a\u0627\u0646'), (b'third', '\u0633\u0648\u0645 \u062f\u0628\u06cc\u0631\u0633\u062a\u0627\u0646'), (b'past', '\u067e\u0633 \u062f\u0628\u06cc\u0631\u0633\u062a\u0627\u0646\u06cc')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='school',
            field=models.CharField(max_length=250, null=True, verbose_name='\u0645\u062f\u0631\u0633\u0647', blank=True),
            preserve_default=True,
        ),
    ]
