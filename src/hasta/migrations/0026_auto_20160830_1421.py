# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0025_auto_20160830_1413"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hasta",
            name="slug",
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
