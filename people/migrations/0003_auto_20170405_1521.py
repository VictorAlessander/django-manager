# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170405_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpeople',
            old_name='sex',
            new_name='gender',
        ),
    ]
