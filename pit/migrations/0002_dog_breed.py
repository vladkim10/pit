# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='breed',
            field=models.CharField(default='Dvor', max_length=1000),
        ),
    ]
