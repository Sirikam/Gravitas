# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-04-05 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170403_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]
