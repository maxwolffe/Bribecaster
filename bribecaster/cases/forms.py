from models import Citizen, User, Case, OBCFormResponse, Case, Office
from django.forms import ModelForm
from django.forms import Form
from django import forms



class CitizenForm(ModelForm):
  class Meta:
    model = Citizen
    fields = '__all__'
    widgets = {
		'first_name': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'text','placeholder': 'Required'}),
		'last_name': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'text','placeholder': 'Required'}),
		'phone_number': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'text'}),
		'aadhaar_number': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'number'}),
		'age': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'number','placeholder': 'Required'}),
		'gender': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'select','placeholder': 'Required'}),
		'address': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'text','placeholder': 'Required'}),
		'city': forms.TextInput(attrs={'class': 'form-control', 
		'type': 'text','placeholder': 'Required'}),
    }


class OBCFormForm(ModelForm):
  class Meta:
    model = OBCFormResponse
    exclude = ('citizen', 'office_visit')

class AadhaarLookup(Form):
	aadhaar_number = forms.IntegerField(label='Aadhaar Number')


class CaseForm(ModelForm):
  pass
#     class Meta: 
#         model = Case 
#         fields = '__all__'
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 
#               'type': 'text','placeholder': 'Required'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 
#               'type': 'text','placeholder': 'Required'}),
#             'phone_number': forms.TextInput(attrs={'class': 'form-control', 
#               'type': 'text'}),
#             'service': forms.TextInput(attrs={'class': 'form-control', 
#               'type': 'text'}),
#             'aadhaar_number': forms.TextInput(attrs={'class': 'form-control', 
#               'type': 'number'}),
#         }
