# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170619_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='user/default.jpg', upload_to='user/img'),
        ),
    ]