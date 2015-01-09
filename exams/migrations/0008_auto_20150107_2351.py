# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20150107_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['order'], 'verbose_name': 'Choice', 'verbose_name_plural': 'Choices'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.CharField(max_length=10000, verbose_name='Choice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False, help_text=b'Is this a correct answer to question?', verbose_name=b'Correct'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='order',
            field=models.IntegerField(help_text='Choices will be shown based on their index. Also this index is shown as choice number in exam page', verbose_name="Choice's index"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(verbose_name=b'Related question', to='exams.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(verbose_name='Related exam', to='exams.Exam'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(help_text="Questions will be shown based on their index. Also this index is shown as the question's number in exam page", unique=True, verbose_name="Question's index"),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set([('question', 'order')]),
        ),
    ]
