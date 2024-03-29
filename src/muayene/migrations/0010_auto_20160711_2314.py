# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0003_auto_20160702_2048"),
        ("muayene", "0009_laboratuvar"),
    ]

    operations = [
        migrations.CreateModel(
            name="LaboratuvarIstek",
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
                ("tarih", models.DateField(default=django.utils.timezone.now)),
                (
                    "hasta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hasta.Hasta"
                    ),
                ),
                ("istek", models.ManyToManyField(to="muayene.Laboratuvar")),
            ],
        ),
        migrations.RenameField(
            model_name="muayene",
            old_name="muayene_tarihi",
            new_name="tarih",
        ),
        migrations.RenameField(
            model_name="rapor",
            old_name="yazilma_tarihi",
            new_name="tarih",
        ),
        migrations.RenameField(
            model_name="recete",
            old_name="yazilma_tarihi",
            new_name="tarih",
        ),
        migrations.AddField(
            model_name="rapor",
            name="rapor_gun",
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="rapor",
            name="tani",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name="muayene",
            name="istenen_tetkikler",
        ),
        migrations.AddField(
            model_name="muayene",
            name="istenen_tetkikler",
            field=models.ManyToManyField(to="muayene.Laboratuvar"),
        ),
        migrations.RemoveField(
            model_name="muayene",
            name="kullandigi_ilaclar",
        ),
        migrations.AddField(
            model_name="muayene",
            name="kullandigi_ilaclar",
            field=models.ManyToManyField(to="muayene.Ilac"),
        ),
        migrations.AddField(
            model_name="laboratuvaristek",
            name="muayene",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="muayene.Muayene"
            ),
        ),
    ]
