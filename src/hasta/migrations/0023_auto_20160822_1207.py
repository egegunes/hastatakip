# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0022_auto_20160820_1513"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hasta",
            name="kayit_tarihi",
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]
