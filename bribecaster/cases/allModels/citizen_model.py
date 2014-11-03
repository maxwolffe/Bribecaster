from django.db import models
from django import forms

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

	region = models.ForeignKey(Region)

class CitizenForm(forms.Form):
	first_name = forms.CharField(label = "First Name", max_length = 40)
	last_name = forms.CharField(label = "Last Name", max_length = 40)
	phone_number = forms.CharField(label = "Phone Number", max_length = 20)
	address = forms.CharField(label = "Address", max_length = 30)
	city = forms.CharField(label = "City", max_length = 30)

