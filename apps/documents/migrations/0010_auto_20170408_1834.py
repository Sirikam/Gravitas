# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-04-08 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_auto_20170407_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
