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
            name='Examples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input', models.TextField(max_length=1000)),
                ('output', models.TextField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.IntegerField(default=0)),
                ('notes', models.TextField(max_length=1000)),
                ('test_input', models.TextField(max_length=1000)),
                ('correct_test_output', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted_output', models.TextField(default=b'')),
                ('result', models.NullBooleanField(default=None)),
                ('question', models.ForeignKey(to='acm.Questions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='submissions',
            name='user',
            field=models.ForeignKey(to='acm.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='examples',
            name='question',
            field=models.ForeignKey(to='acm.Questions'),
            preserve_default=True,
        ),
    ]
