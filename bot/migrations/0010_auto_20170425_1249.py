# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-04-25 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_user_positionname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='positionName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
