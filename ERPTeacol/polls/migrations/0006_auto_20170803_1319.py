# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_delete_customerorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=15)),
                ('preformance', models.CharField(max_length=250)),
                ('places', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerRecord',
        ),
    ]
