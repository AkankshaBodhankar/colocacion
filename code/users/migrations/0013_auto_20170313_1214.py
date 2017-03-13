# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170313_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_id', models.IntegerField()),
                ('choice_text', models.CharField(max_length=1000)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Questions')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tests')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='choices',
            unique_together=set([('test_id', 'question_id', 'choice_id')]),
        ),
    ]
