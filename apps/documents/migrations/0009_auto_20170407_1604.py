# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-04-07 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_auto_20170405_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
