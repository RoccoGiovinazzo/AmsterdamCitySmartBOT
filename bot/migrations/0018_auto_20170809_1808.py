# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-08-09 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_auto_20170809_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='maxHours',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
