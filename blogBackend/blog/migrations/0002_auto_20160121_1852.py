# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
