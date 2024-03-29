# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160614095717 on 2016-07-09 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0003_auto_20160702_2048"),
        ("muayene", "0007_auto_20160708_1715"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ilac",
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
                ("ad", models.CharField(max_length=30)),
                ("bilgi", models.CharField(max_length=30)),
                ("kullanim", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Rapor",
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
                ("yazilma_tarihi", models.DateField(default=django.utils.timezone.now)),
                (
                    "hasta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hasta.Hasta"
                    ),
                ),
                (
                    "muayene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="muayene.Muayene",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recete",
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
                ("yazilma_tarihi", models.DateField(default=django.utils.timezone.now)),
                (
                    "hasta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hasta.Hasta"
                    ),
                ),
                ("ilaclar", models.ManyToManyField(to="muayene.Ilac")),
                (
                    "muayene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="muayene.Muayene",
                    ),
                ),
            ],
        ),
    ]
