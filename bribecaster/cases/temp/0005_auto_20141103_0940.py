# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_auto_20141103_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officevisit',
            name='time_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 40, 45, 330248)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='robocallfeedback',
            name='time_of_call',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 40, 45, 330908)),
            preserve_default=True,
        ),
    ]
