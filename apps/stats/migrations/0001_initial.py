# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-17 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntranetMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IntranetMachineStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('os_name', models.CharField(max_length=20)),
                ('mem_usage', models.FloatField()),
                ('cpu_usage', models.FloatField()),
                ('total_uptime', models.FloatField()),
                ('intranet_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.IntranetMachine')),
            ],
        ),
    ]