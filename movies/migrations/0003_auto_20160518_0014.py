# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160517_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_loc',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]