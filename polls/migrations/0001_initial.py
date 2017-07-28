# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('phone', models.IntegerField(primary_key=True, serialize=False)),
                ('preformance', models.CharField(max_length=250)),
                ('places', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('add_phone', models.IntegerField()),
                ('adress', models.CharField(max_length=150)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.CustomerOrders')),
            ],
        ),
    ]