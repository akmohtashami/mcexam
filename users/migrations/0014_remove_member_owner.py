# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_member_exam_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='owner',
        ),
    ]
