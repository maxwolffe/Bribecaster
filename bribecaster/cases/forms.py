from models import Citizen, User, Case, OBCForm, Case, Office
from django.forms import ModelForm


class CitizenForm(ModelForm):
  class Meta:
    model = Citizen
    exclude = ('region')

class 


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
