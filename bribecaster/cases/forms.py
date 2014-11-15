from models import Citizen, User, Case, OBCFormResponse, Case, Office
from django.forms import ModelForm


class CitizenForm(ModelForm):
  class Meta:
    model = Citizen

class OBCFormForm(ModelForm):
  class Meta:
    model = OBCFormResponse
    exclude = ('citizen', 'office_visit')


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
