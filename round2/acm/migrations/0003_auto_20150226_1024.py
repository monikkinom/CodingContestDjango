# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0002_mcqquestions_mcqsubmissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqquestions',
            name='notes',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='mcqquestions',
            name='optiona',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='mcqquestions',
            name='optionb',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='mcqquestions',
            name='optionc',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='mcqquestions',
            name='optiond',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='correct_test_output',
            field=models.TextField(max_length=5000000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='notes',
            field=models.TextField(max_length=5000000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='test_input',
            field=models.TextField(max_length=5000000),
        ),
    ]
