# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='date_of_send',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
