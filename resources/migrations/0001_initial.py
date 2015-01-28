# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import resources.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_object_id', models.PositiveIntegerField()),
                ('is_private', models.BooleanField(help_text='Private resources are not served by webserver', verbose_name='Private')),
                ('filename', models.CharField(max_length=1000, verbose_name='File Name', blank=True)),
                ('resource', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/'), upload_to=resources.models.get_upload_path)),
                ('owner_content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
