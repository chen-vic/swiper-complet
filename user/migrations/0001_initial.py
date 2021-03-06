# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-03 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=16, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('gender', models.CharField(max_length=10, verbose_name='性别')),
                ('birthday', models.DateField(default='1990-01-01', verbose_name='生日')),
                ('avatar', models.CharField(max_length=256, verbose_name='个人形象')),
                ('location', models.CharField(max_length=20, verbose_name='常居地')),
            ],
        ),
    ]
