# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20161217_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]