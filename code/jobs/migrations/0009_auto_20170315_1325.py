# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_jobsapplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_title',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
