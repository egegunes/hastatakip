# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0032_sozlesme_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hasta",
            name="sigorta",
            field=models.CharField(blank=True, default="", max_length=30),
        ),
    ]
