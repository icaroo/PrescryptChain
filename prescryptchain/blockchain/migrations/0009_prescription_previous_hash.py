# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0008_block_merkleroot'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='previous_hash',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]