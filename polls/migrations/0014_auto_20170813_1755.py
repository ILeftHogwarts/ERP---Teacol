# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_remove_theatreinfo_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorders',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='customerorders',
            name='theatre_info',
        ),
        migrations.DeleteModel(
            name='CustomerOrders',
        ),
    ]
