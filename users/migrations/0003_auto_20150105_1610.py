# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150105_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
