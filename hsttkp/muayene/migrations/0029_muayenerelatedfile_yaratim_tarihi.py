# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('muayene', '0028_auto_20160824_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='muayenerelatedfile',
            name='yaratim_tarihi',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]
