# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("muayene", "0024_auto_20160823_1227"),
    ]

    operations = [
        migrations.AddField(
            model_name="recete",
            name="ilac1_kutu",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac2_kutu",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac3_kutu",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac4_kutu",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name="recete",
            name="ilac5_kutu",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
