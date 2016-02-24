# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 03:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='gnome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Gnome'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gnome',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gnomes', to=settings.AUTH_USER_MODEL),
        ),
    ]
