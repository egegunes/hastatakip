# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0033_auto_20160919_2143"),
    ]

    operations = [
        migrations.AddField(
            model_name="hasta",
            name="ahsevk_done_tarih",
            field=models.DateField(
                blank=True, default=django.utils.timezone.now, editable=False, null=True
            ),
        ),
    ]
