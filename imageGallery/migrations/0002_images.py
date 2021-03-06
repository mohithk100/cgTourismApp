# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imageGallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageGallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=imageGallery.models.get_upload_url)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='imageGallery.ImageGallery')),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
    ]
