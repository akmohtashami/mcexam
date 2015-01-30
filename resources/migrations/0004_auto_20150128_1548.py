# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import resources.models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20150128_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/'), max_length=5000, upload_to=resources.models.get_upload_path),
            preserve_default=True,
        ),
    ]
