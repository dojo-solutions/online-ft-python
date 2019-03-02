# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-01 17:07
from __future__ import unicode_literals

from django.db import migrations, models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.now()),
            preserve_default=False,
        ),
    ]