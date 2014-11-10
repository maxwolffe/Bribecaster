# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('office_head', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('speed_rating', models.IntegerField()),
                ('cost_rating', models.IntegerField()),
                ('quality_rating', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfficeVisit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_used', models.CharField(max_length=1, choices=[(b'0', b'fard'), (b'1', b'domicile'), (b'2', b'marriage'), (b'3', b'divorce')])),
                ('case', models.ForeignKey(to='cases.Case')),
                ('citizen', models.ForeignKey(to='cases.Citizen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aggregate_cost_rating', models.IntegerField()),
                ('aggregate_quality_rating', models.IntegerField()),
                ('aggregate_speed_rating', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoboCallFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_response', models.CharField(max_length=1, choices=[(b'0', b'picked-up'), (b'1', b'busy'), (b'2', b'voicemail'), (b'3', b'not-a-number')])),
                ('case', models.ForeignKey(to='cases.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SMSFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_sent_time', models.DateTimeField()),
                ('message_recieved_time', models.DateTimeField()),
                ('sms_sent_text', models.CharField(max_length=140)),
                ('sms_recieved_text', models.CharField(max_length=280)),
                ('case', models.ForeignKey(to='cases.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('employee_number', models.IntegerField()),
                ('office', models.ForeignKey(to='cases.Office')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='office',
            name='region',
            field=models.ForeignKey(to='cases.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='citizen',
            name='region',
            field=models.ForeignKey(to='cases.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='aadhaar_number',
            field=models.BigIntegerField(default=0, max_length=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='citizen',
            field=models.ForeignKey(default=1, to='cases.Citizen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='office',
            field=models.ForeignKey(default=1, to='cases.Office'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ManyToManyField(default=1, to='cases.User'),
            preserve_default=True,
        ),
    ]
