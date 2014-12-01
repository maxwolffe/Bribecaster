# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20141103_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='aadhaar_number',
        ),
        migrations.RemoveField(
            model_name='case',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='case',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='case',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='case',
            name='service',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=b'Unassigned', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officevisit',
            name='time_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 11, 7, 54, 321616)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='robocallfeedback',
            name='time_of_call',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 11, 7, 54, 322254)),
            preserve_default=True,
        ),
    ]
