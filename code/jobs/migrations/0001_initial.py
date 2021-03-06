# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20170220_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=300)),
                ('job_type', models.CharField(max_length=100)),
                ('experience_required', models.CharField(max_length=500)),
                ('company_name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=500)),
                ('skills_set', models.CharField(max_length=1000)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='JobsApplied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserDetails')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Jobs')),
            ],
        ),
    ]
