# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import downloads.models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0002_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTB_Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pdf', models.FileField(upload_to=downloads.models.get_ctb_upload_url)),
            ],
            options={
                'verbose_name_plural': 'CTB_NewsLetters',
            },
        ),
        migrations.CreateModel(
            name='ImportantDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pdf', models.FileField(upload_to=downloads.models.get_id_upload_url)),
            ],
            options={
                'verbose_name_plural': 'Important Documents',
            },
        ),
        migrations.CreateModel(
            name='RegisterationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pdf', models.FileField(upload_to=downloads.models.get_rf_upload_url)),
            ],
            options={
                'verbose_name_plural': 'Registeration Forms',
            },
        ),
    ]
