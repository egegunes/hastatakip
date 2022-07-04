# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0014_auto_20160801_1241"),
        ("muayene", "0019_auto_20160731_1538"),
    ]

    operations = [
        migrations.CreateModel(
            name="MuayeneRelatedFile",
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
                ("dosya", models.FileField(upload_to="uploads/%Y/%m/%d/")),
                (
                    "hasta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hasta.Hasta"
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="muayene",
            old_name="öneri_görüsler",
            new_name="oneri_gorusler",
        ),
        migrations.RenameField(
            model_name="muayene",
            old_name="öntani_tani",
            new_name="ontani_tani",
        ),
        migrations.RenameField(
            model_name="muayene",
            old_name="özel_notlar",
            new_name="ozel_notlar",
        ),
        migrations.AddField(
            model_name="muayenerelatedfile",
            name="muayene",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="muayene.Muayene"
            ),
        ),
    ]
