# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-22 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170322_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]