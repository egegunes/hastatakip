# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("muayene", "0027_auto_20160823_1656"),
    ]

    operations = [
        migrations.AlterField(
            model_name="laboratuvaristek",
            name="og11",
            field=models.BooleanField(
                default=False,
                verbose_name="OGTT (75 gr Glikoz ile 0-60-120-180 dakikalarda)",
            ),
        ),
    ]
