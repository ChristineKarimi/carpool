# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 07:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver', '0002_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_riders', models.IntegerField()),
                ('needed_riders', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.DateField(blank=True, null=True, verbose_name='DOB')),
                ('registration', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default=False, upload_to='vehicle-image/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]