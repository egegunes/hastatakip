# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muayene', '0033_auto_20160922_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom1_ad',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom1_sonuc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom2_ad',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom2_sonuc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom3_ad',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom3_sonuc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom4_ad',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom4_sonuc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom5_ad',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='laboratuvaristek',
            name='custom5_sonuc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
