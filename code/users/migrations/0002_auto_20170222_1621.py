# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='level',
            field=models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('difficult', 'difficult')], max_length=10),
        ),
    ]