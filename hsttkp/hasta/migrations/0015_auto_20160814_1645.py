# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-14 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hasta', '0014_auto_20160801_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sozlesme',
            options={'get_latest_by': 'baslangic_tarihi'},
        ),
    ]
