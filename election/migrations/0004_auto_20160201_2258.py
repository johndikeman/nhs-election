# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_auto_20160201_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='answeredQuestions',
            field=models.ManyToManyField(blank=True, to='election.Question'),
        ),
    ]