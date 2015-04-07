# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='McqQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.IntegerField(default=0)),
                ('notes', models.TextField(max_length=1000)),
                ('optiona', models.TextField(max_length=1000)),
                ('optionb', models.TextField(max_length=1000)),
                ('optionc', models.TextField(max_length=1000)),
                ('optiond', models.TextField(max_length=1000)),
                ('correct_ans', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='McqSubmissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted_output', models.IntegerField(default=0)),
                ('result', models.NullBooleanField(default=None)),
                ('question', models.ForeignKey(to='acm.McqQuestions')),
                ('user', models.ForeignKey(to='acm.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
