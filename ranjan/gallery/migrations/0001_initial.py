# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateTimeField(verbose_name='datetime')),
                ('img', models.ImageField(upload_to='static/tmp')),
            ],
        ),
    ]