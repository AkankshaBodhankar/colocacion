# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20170313_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_id', models.IntegerField()),
                ('choice_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('question_text', models.CharField(max_length=1000)),
                ('correct_choice', models.CharField(max_length=1000)),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tests')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Questions'),
        ),
        migrations.AddField(
            model_name='choice',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tests'),
        ),
        migrations.AlterUniqueTogether(
            name='questions',
            unique_together=set([('test_id', 'question_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set([('test_id', 'question_id', 'choice_id')]),
        ),
    ]
