# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("muayene", "0023_auto_20160822_1206"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="laboratuvaristek",
            name="istekler",
        ),
        migrations.RemoveField(
            model_name="recete",
            name="ilaclar",
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac1",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ilac1",
                to="muayene.Ilac",
            ),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac1_kullanim",
            field=models.CharField(default="Günde 1", max_length=100),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ilac2",
                to="muayene.Ilac",
            ),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac2_kullanim",
            field=models.CharField(blank=True, default=" ", max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ilac3",
                to="muayene.Ilac",
            ),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac3_kullanim",
            field=models.CharField(blank=True, default=" ", max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ilac4",
                to="muayene.Ilac",
            ),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac4_kullanim",
            field=models.CharField(blank=True, default=" ", max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac5",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ilac5",
                to="muayene.Ilac",
            ),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac5_kullanim",
            field=models.CharField(blank=True, default=" ", max_length=100, null=True),
        ),
    ]
