# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170307_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='test_id',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
