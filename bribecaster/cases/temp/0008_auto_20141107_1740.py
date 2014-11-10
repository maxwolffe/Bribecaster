# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20141103_1107'),
    ]

    operations = [
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
            name='OBCForm',
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
            name='age',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='citizen',
            name='gender',
            field=models.CharField(default=b'unkown', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officevisit',
            name='time_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 17, 40, 42, 930799)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='robocallfeedback',
            name='time_of_call',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 17, 40, 42, 933089)),
            preserve_default=True,
        ),
    ]
