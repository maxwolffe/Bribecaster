# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


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
                ('gender', models.CharField(default=b'unkown', max_length=20)),
                ('age', models.IntegerField(default=-1)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('aadhaar_number', models.BigIntegerField(default=-1, max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OBCFormResponse',
            fields=[
                ('form_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cases.Form')),
                ('religion', models.CharField(max_length=40)),
                ('caste', models.CharField(max_length=40)),
                ('sub_caste', models.CharField(max_length=40)),
                ('issued_in_past', models.BooleanField()),
                ('education_certification_contains_caste', models.BooleanField()),
                ('caste_serial_number', models.CharField(max_length=40)),
                ('name_of_father', models.CharField(default=b'NA', max_length=40)),
                ('name_of_mother', models.CharField(default=b'NA', max_length=40)),
                ('name_of_husband', models.CharField(default=b'NA', max_length=40)),
                ('male_status', models.CharField(default=b'NA', max_length=180)),
                ('female_status', models.CharField(default=b'NA', max_length=180)),
                ('org_status', models.CharField(default=b'NA', max_length=180)),
                ('death_details', models.CharField(default=b'NA', max_length=180)),
                ('public_service_details', models.CharField(default=b'NA', max_length=180)),
                ('land_holding', models.CharField(default=b'NA', max_length=40)),
                ('land_location', models.CharField(default=b'NA', max_length=40)),
                ('other_land_information', models.CharField(default=b'NA', max_length=180)),
                ('plantation_information', models.CharField(default=b'NA', max_length=180)),
                ('annual_income', models.IntegerField()),
                ('tax_paid', models.BooleanField()),
                ('purpose_of_certificate', models.CharField(default=b'NA', max_length=180)),
                ('ration_card_number', models.CharField(default=b'NA', max_length=40)),
                ('final_notes', models.CharField(default=b'NA', max_length=180)),
            ],
            options={
            },
            bases=('cases.form',),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_name', models.CharField(default=b'default Office', max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('office_head', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('speed_rating', models.IntegerField(default=-1)),
                ('cost_rating', models.IntegerField(default=-1)),
                ('quality_rating', models.IntegerField(default=-1)),
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
                ('time_of_visit', models.DateTimeField(default=datetime.datetime(2014, 11, 8, 0, 7, 12, 198118))),
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
                ('region_name', models.CharField(default=b'Unnamed', max_length=30)),
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
                ('time_of_call', models.DateTimeField(default=datetime.datetime(2014, 11, 8, 0, 7, 12, 198651))),
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
                ('role', models.CharField(default=b'Unassigned', max_length=30)),
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
            model_name='form',
            name='citizen',
            field=models.ForeignKey(to='cases.Citizen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='form',
            name='office_visit',
            field=models.ForeignKey(to='cases.OfficeVisit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='citizen',
            name='region',
            field=models.ForeignKey(to='cases.Region'),
            preserve_default=True,
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
            field=models.ManyToManyField(default=[1], to='cases.User'),
            preserve_default=True,
        ),
    ]
