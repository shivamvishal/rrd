# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20171025_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
