# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-21 18:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='role_in_app',
            field=models.CharField(default='ST', max_length=2),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]