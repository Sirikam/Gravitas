# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-04-07 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170405_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]
