# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-22 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20170322_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
