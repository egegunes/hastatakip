# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0034_hasta_ahsevk_done_tarih'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hasta',
            name='cinsiyet',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('K', 'Kadın'), ('E', 'Erkek')], max_length=5),
        ),
    ]
