# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-04-20 15:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20170420_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
