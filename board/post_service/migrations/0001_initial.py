# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regdate', models.DateTimeField(auto_created=True, auto_now_add=True)),
            ],
        ),
    ]
