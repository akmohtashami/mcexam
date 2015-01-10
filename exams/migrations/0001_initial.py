# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=10000, verbose_name='\u06af\u0632\u06cc\u0646\u0647')),
                ('order', models.IntegerField(help_text='\u06af\u0632\u06cc\u0646\u0647 \u0647\u0627 \u0628\u0631\u0627\u0633\u0627\u0633 \u0634\u0645\u0627\u0631\u0647 \u0634\u0627\u0646 \u0645\u0631\u062a\u0628 \u0648 \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0645\u06cc \u0634\u0648\u0646\u062f', verbose_name='\u0634\u0645\u0627\u0631\u0647 \u06af\u0632\u06cc\u0646\u0647')),
                ('is_correct', models.BooleanField(default=False, help_text=b'Is this a correct answer to question?', verbose_name=b'Correct')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u06af\u0632\u06cc\u0646\u0647',
                'verbose_name_plural': '\u06af\u0632\u06cc\u0646\u0647 \u0647\u0627',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='\u0646\u0627\u0645 \u0622\u0632\u0645\u0648\u0646')),
                ('start_date', models.DateTimeField(verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0634\u0631\u0648\u0639')),
                ('end_date', models.DateTimeField(verbose_name='\u062a\u0627\u0631\u06cc\u062e \u067e\u0627\u06cc\u0627\u0646')),
            ],
            options={
                'verbose_name': '\u0622\u0632\u0645\u0648\u0646',
                'verbose_name_plural': '\u0622\u0632\u0645\u0648\u0646 \u0647\u0627',
                'permissions': (('can_view', '\u06a9\u0627\u0631\u0628\u0631 \u062a\u0648\u0627\u0646\u0627\u06cc\u06cc \u062f\u06cc\u062f\u0646 \u0622\u0632\u0645\u0648\u0646 \u0647\u0627 \u0631\u0627 \u062f\u0627\u0631\u062f'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MadeChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.ForeignKey(to='exams.Choice')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(help_text='\u0633\u0648\u0627\u0644\u0627\u062a \u0628\u0631\u0627\u0633\u0627\u0633 \u0634\u0645\u0627\u0631\u0647 \u0634\u0627\u0646 \u0645\u0631\u062a\u0628 \u0648 \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0645\u06cc \u0634\u0648\u0646\u062f', unique=True, verbose_name='\u0634\u0645\u0627\u0631\u0647 \u06cc \u0633\u0648\u0627\u0644')),
                ('statement', models.CharField(max_length=10000, verbose_name='\u0635\u0648\u0631\u062a \u0633\u0648\u0627\u0644')),
                ('exam', models.ForeignKey(verbose_name='\u0622\u0632\u0645\u0648\u0646 \u0645\u0631\u0628\u0648\u0637\u0647', to='exams.Exam')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u0633\u0648\u0627\u0644',
                'verbose_name_plural': '\u0633\u0648\u0627\u0644\u0627\u062a',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(verbose_name=b'Related question', to='exams.Question'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set([('question', 'order')]),
        ),
    ]
