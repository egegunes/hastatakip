# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muayene', '0008_ilac_rapor_recete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratuvar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=30)),
            ],
        ),
    ]
