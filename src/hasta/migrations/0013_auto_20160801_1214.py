# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0012_auto_20160731_1857"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hasta",
            name="aile",
            field=models.ForeignKey(
                blank=True,
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="hasta.Aile",
            ),
        ),
    ]
