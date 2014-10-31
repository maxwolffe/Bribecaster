from django.db import models
from django.forms import ModelForm
from django import forms

""" A Case Model containing the forms and followups from a particular citizen visit to an office.

belongs to a user
belongs to an office
"""
class Case(models.Model):
    #customer_information
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    phone_number = models.CharField(max_length = 20)
    service = models.CharField(max_length = 50)
    
    sms_selected = models.BooleanField()
    robo_call_selected = models.BooleanField()
    follow_up_selected = models.BooleanField()

    # sms_response = models.ManyToManyField(SMSResponse)
    # robo_response = models.ForeignKey(RoboResponse)
    # call_response = models.ManyToManyField(CallResponse)

    # citizen = models.ForeignKey(Citizen)
    # office = models.ForeignKey(Office)
    # user = models.ManyToMany(User)

class CaseForm(ModelForm):
    class Meta: 
        model = Case 
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text'}),
            'service': forms.TextInput(attrs={'class': 'form-control', 
              'type': 'text'}),
        }