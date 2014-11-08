# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20141103_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='office_name',
            field=models.CharField(default=b'default Office', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='officevisit',
            name='time_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 33, 31, 629218)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='region',
            name='region_name',
            field=models.CharField(default=b'Unnamed', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='robocallfeedback',
            name='time_of_call',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 9, 33, 31, 629842)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='cost_rating',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='quality_rating',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='speed_rating',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
