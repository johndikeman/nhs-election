# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0005_question_spec'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='time_limit',
            field=models.IntegerField(default=72),
        ),
    ]