# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 14:18
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160622_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libuser',
            name='profilepic',
            field=sorl.thumbnail.fields.ImageField(default='/app/static/ProfilePics/defaultpic.png', upload_to='app/static/ProfilePics/'),
        ),
    ]
