# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-09 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("randevu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="randevu",
            name="state",
            field=models.CharField(
                choices=[(1, "Açık"), (2, "İptal")], default=1, max_length=1
            ),
            preserve_default=False,
        ),
    ]
