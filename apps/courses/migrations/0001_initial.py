# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-02-23 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=25)),
                ('course_name', models.CharField(max_length=50)),
                ('lecturer', models.CharField(max_length=150)),
            ],
        ),
    ]
