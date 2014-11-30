# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=20)),
                ('service', models.CharField(max_length=50)),
                ('sms_selected', models.BooleanField()),
                ('robo_call_selected', models.BooleanField()),
                ('follow_up_selected', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
