# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-22 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170322_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]