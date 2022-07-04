# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("muayene", "0016_auto_20160725_2313"),
    ]

    operations = [
        migrations.RenameField(
            model_name="laboratuvaristek",
            old_name="istek",
            new_name="istekler",
        ),
        migrations.AlterField(
            model_name="muayene",
            name="muayene",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="muayene",
            name="yakinma",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="muayene",
            name="öneri_görüsler",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="muayene",
            name="öntani_tani",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="muayene",
            name="özel_notlar",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
