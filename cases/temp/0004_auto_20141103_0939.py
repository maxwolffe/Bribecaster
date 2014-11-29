# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20141103_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='aadhaar_number',
            field=models.BigIntegerField(default=-1, max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officevisit',
            name='time_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 39, 53, 53933)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='robocallfeedback',
            name='time_of_call',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 39, 53, 54557)),
            preserve_default=True,
        ),
    ]
