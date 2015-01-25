# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0017_auto_20150124_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_pdf_template',
            field=models.TextField(default=b'', help_text='Django-Tex template for creating pdf files', verbose_name='PDF template'),
            preserve_default=True,
        ),
    ]
