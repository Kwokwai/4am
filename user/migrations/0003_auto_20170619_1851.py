# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170619_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, default='user/default.jpg', upload_to='user/img'),
        ),
    ]
