from django.db import models
from django.forms import ModelForm
from django import forms
from datetime import datetime

SERVICE_TYPE = (
    ('0', 'fard'),
    ('1', 'domicile'),
    ('2', 'marriage'),
    ('3', 'divorce'),
)

RESPONSE_TYPE = (
    ('0', 'picked-up'),
    ('1', 'busy'),
    ('2', 'voicemail'),
    ('3', 'not-a-number'),
)

DEFAULT = 1

""" Model Representing a region
aggregate_speed_rating - int
aggregate_quality_rating - int
aggregate_cost_rating - int 

has_many offices
has_many citizens

"""
class Region(models.Model):
    region_name = models.CharField(max_length = 30, default = "Unnamed")
    aggregate_cost_rating = models.IntegerField()
    aggregate_quality_rating = models.IntegerField()
    aggregate_speed_rating = models.IntegerField()

    def __str__(self):
        return self.region_name

""" A Citizen Model representing citizens who visit the office

has_many cases
belong_to region

"""
class Citizen(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    phone_number = models.CharField(max_length = 20)
    address = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    aadhaar_number = models.BigIntegerField(max_length = 12, default = -1)


    region = models.ForeignKey(Region)

    def __str__(self):
        return self.first_name + " " + self.last_name + " : " + self.phone_number


""" Represents an Office:
Has many cases, users (employees)
Belongs to a region


"""
class Office(models.Model):
    office_name = models.CharField(max_length = 30, default = "default Office")
    address = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 20)
    office_head = models.CharField(max_length = 30) # Should maybe be a user
    lat = models.FloatField()
    lon = models.FloatField()

    speed_rating = models.IntegerField(default = -1)
    cost_rating = models.IntegerField(default = -1)
    quality_rating = models.IntegerField(default = -1)
    
    region = models.ForeignKey(Region)

    def __str__(self):
        return self.office_name

""" A User Model representing an employee of the government. 

"""
class User(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    role = models.CharField(max_length = 30, default = "Unassigned") #we can probably make this a drop down later. (data input, manager, etc)
    employee_number = models.IntegerField()

    office = models.ForeignKey(Office)

    def __str__(self):
        return self.first_name + " " + self.last_name + " at " + self.office.office_name

""" A Case Model containing the forms and followups from a particular citizen visit to an office.

belongs to a user
belongs to an office
"""
class Case(models.Model):
    #customer_information

    citizen = models.ForeignKey(Citizen, default = DEFAULT)
    office = models.ForeignKey(Office, default = DEFAULT)
    user = models.ManyToManyField(User, default = [DEFAULT])
    
    sms_selected = models.BooleanField()
    robo_call_selected = models.BooleanField()
    follow_up_selected = models.BooleanField()

    # sms_response = models.ManyToManyField(SMSResponse)
    # robo_response = models.ForeignKey(RoboResponse)
    # call_response = models.ManyToManyField(CallResponse)

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + " " + self.last_name + ";" + self.phone_number + ";" + self.service

class OfficeVisit(models.Model):
    service_used = models.CharField(max_length = 1, choices = SERVICE_TYPE)
    time_of_visit = models.DateTimeField(default = datetime.now())

    case = models.ForeignKey(Case)
    citizen = models.ForeignKey(Citizen)

    def __str__(self):
        return str(self.citizen.aadhaar_number) + " : " + " Office Visit on " + str(self.time_of_visit)


class RoboCallFeedback(models.Model):
    call_response = models.CharField(max_length=1, choices=RESPONSE_TYPE)
    time_of_call = models.DateTimeField(default = datetime.now())

    case = models.ForeignKey(Case)

    def __str__(self):
        return "RoboCall"

class SMSFeedback(models.Model):
    message_sent_time = models.DateTimeField()
    message_recieved_time = models.DateTimeField()
    sms_sent_text = models.CharField(max_length = 140)
    sms_recieved_text = models.CharField(max_length = 280) #Can we get longer responses?

    case = models.ForeignKey(Case)

    def __str__(self):
        return "SMSFeedback"

"""
class CaseForm(ModelForm):
    class Meta: 
        model = Case 
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text','placeholder': 'Required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text','placeholder': 'Required'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text'}),
            'service': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text'}),
            'aadhaar_number': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'number'}),
        }
"""

