# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['date_joined'], 'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
        migrations.AlterModelOptions(
            name='usersbook',
            options={'ordering': ['id'], 'verbose_name': 'Книга пользователя', 'verbose_name_plural': 'Книги пользователей'},
        ),
    ]