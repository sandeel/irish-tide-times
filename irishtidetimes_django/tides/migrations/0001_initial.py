# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=20)),
                ('first_low', models.TimeField(null=True)),
                ('first_high', models.TimeField(null=True)),
                ('second_low', models.TimeField(null=True)),
                ('second_high', models.TimeField(null=True)),
            ],
        ),
    ]