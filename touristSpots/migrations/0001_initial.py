# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import touristSpots.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=touristSpots.models.get_upload_url)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=2500)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='placeimages',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='touristSpots.Places'),
        ),
    ]
