# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20141103_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='user',
            field=models.ManyToManyField(default=[1], to='cases.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officevisit',
            name='time_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 48, 24, 776969)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='robocallfeedback',
            name='time_of_call',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 48, 24, 777592)),
            preserve_default=True,
        ),
    ]
