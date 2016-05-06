# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('review', models.TextField(blank=True, null=True)),
                ('date_reviewd', models.DateTimeField(blank=True, null=True)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]