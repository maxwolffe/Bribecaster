# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_auto_20141107_1740'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OBCForm',
            new_name='OBCFormResponse',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='region',
        ),
        migrations.RemoveField(
            model_name='office',
            name='region',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.AlterField(
            model_name='officevisit',
            name='time_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 8, 18, 7, 55, 958751)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='robocallfeedback',
            name='time_of_call',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 8, 18, 7, 55, 959672)),
            preserve_default=True,
        ),
    ]
