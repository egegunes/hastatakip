# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0010_auto_20160727_1530"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sozlesme",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sure", models.CharField(blank=True, max_length=10)),
                (
                    "hasta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hasta.Hasta"
                    ),
                ),
            ],
        ),
    ]
