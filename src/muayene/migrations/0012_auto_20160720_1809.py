# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("muayene", "0011_auto_20160717_1407"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="muayene",
            name="istenen_tetkikler",
        ),
        migrations.RemoveField(
            model_name="muayene",
            name="tetkik_sonuclari",
        ),
    ]
