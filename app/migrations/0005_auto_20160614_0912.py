# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 13:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160611_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pubyr', models.IntegerField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Book'), (2, 'DVD'), (3, 'Other')], default=1)),
                ('cost', models.IntegerField()),
                ('num_interested', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='libitem',
            name='date_acquired',
            field=models.DateField(default=datetime.date(2016, 6, 14)),
        ),
    ]