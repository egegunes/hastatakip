# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hasta", "0009_auto_20160720_1313"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hasta",
            name="adres",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="boy",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="cep_telefon",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="eposta",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="ev_telefon",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="is_telefon",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="kilo",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="ozgecmis",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="soygecmis",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="hasta",
            name="tc_kimlik_no",
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
