from models import Citizen, User, Case, OBCFormResponse, Office, GENDER
from django.forms import ModelForm
from django.forms import Form
from django import forms

RELGIONS = (
	('0', 'Religion Numba One'),
    ('1', 'Great Religion'),
    ('2', 'Another Religion'),
    ('3', 'Best Religion')
)

PAY_SCALE = (
	('0', 'Pay Scale 0'),
    ('1', 'Pay Scale 1'),
    ('2', 'Pay Scale 2'),
    ('3', 'Pay Scale 3'),
    ('4', 'Pay Scale 4')
)

CASTE = (
	('0', 'Caste 1'),
    ('1', 'Caste 2'),
    ('2', 'Caste 3'),
    ('3', 'Caste 4'),
    ('4', 'Caste 5')
)

BOOLEAN = (
	('0', "Yes"),
	('1', "No")
)

DESIGNATIONS = (
	('0', 'Designation 1'),
	('1', 'Designation 2')
)

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
			'type': 'text', 'placeholder': 'Required'}),
		'aadhaar_number': forms.TextInput(attrs={'class': 'form-control', 
			'type': 'number', 'placeholder': 'Required'}),
		'address': forms.TextInput(attrs={'class': 'form-control', 
			'type': 'text','placeholder': 'Required'}),
		'city': forms.TextInput(attrs={'class': 'form-control', 
			'type': 'text','placeholder': 'Required'}),
    'date_of_birth': forms.DateInput(attrs = { 'type': 'date' }),
    'gender': forms.Select(choices = GENDER),
    }


class OBCFormForm(ModelForm):
  class Meta:
    model = OBCFormResponse
    exclude = ('citizen', 'office_visit', 'name_of_husband')
    labels = {
     "religion": "Religion",
     "caste": "Caste",
     "sub_caste": "Sub Caste",
     "issued_in_past": "Issued In Past?" ,
     "education_certification_contains_caste" : "Does the Education Certification contain Caste?",
     "caste_serial_number": "Caste Serial Number",
     "name_of_father": "Name of Father",
     "name_of_mother": "Name of Mother",
     "male_constitutional_posts": "Male Constitutional Posts",
     "male_designation": "Male Designation",
     "male_scale_of_pay": "Male Scale of Pay",
     "male_date_of_start": "Male Start of Appointment",
	 "male_date_of_finish": "Male End of Appointment",
	 "female_constitutional_posts": "Female Constitutional Posts",
     "female_designation": "Female Designation",
     "female_scale_of_pay": "Female Scale of Pay",
     "female_date_of_start": "Female Start of Appointment",
	 "female_date_of_finish": "Female End of Appointment"
     }
    widgets = {
     "religion": forms.Select(choices = RELGIONS), 
     "caste": forms.Select(choices = CASTE), 
     "sub_caste": forms.Select(choices = CASTE),
     "education_certification_contains_caste": forms.Select(choices = BOOLEAN),
     "issued_in_past": forms.Select(choices = BOOLEAN),
     "caste_serial_number": forms.TextInput(attrs={'class': 'form-control', 
			'type': 'number', 'placeholder': 'Required'}),
     "name_of_father": forms.TextInput(attrs={'class': 'form-control', 
			'type': 'text', 'placeholder': 'Required'}),
     "name_of_mother": forms.TextInput(attrs={'class': 'form-control', 
			'type': 'text', 'placeholder': 'Required'}),
     "male_constitutional_posts": forms.TextInput(attrs={'class': 'form-control', 
			'type': 'text', 'placeholder': 'Required'}),
     "female_constitutional_posts": forms.TextInput(attrs={'class': 'form-control', 
			'type': 'text', 'placeholder': 'Required'}),
     "male_designation": forms.Select(choices = DESIGNATIONS),
     "female_designation": forms.Select(choices = DESIGNATIONS),
     "male_scale_of_pay": forms.Select(choices = PAY_SCALE),
     "female_scale_of_pay": forms.Select(choices = PAY_SCALE),
     "male_date_of_start": forms.DateInput(attrs = { 'type': 'date' }),
     "female_date_of_start": forms.DateInput(attrs = { 'type': 'date' }),
     "male_date_of_finish": forms.DateInput(attrs = { 'type': 'date' }),
     "female_date_of_finish": forms.DateInput(attrs = { 'type': 'date' }),
     }

  #    "caste": "Caste",
  #    "sub_caste": "Sub Caste",
  #    "issued_in_past": "Issued In Past?" ,
  #    "education_certification_contains_caste" : "Does the Education Certification contain Caste?",
  #    "caste_serial_number": "Caste Serial Number",
  #    "name_of_father": "Name of Father",
  #    "name_of_mother": "Name of Mother",
  #    "male_consititutional_posts": "Male Constitutional Posts",
  #    "male_designation": "Male Designation",
  #    "male_scale_of_pay": "Male Scale of Pay",
  #    "male_start_of_appointment": "Male Start of Appointment",
	 # "male_end_of_appointment": "Male End of Appointment",
	 # "female_consititutional_posts": "Female Constitutional Posts",
  #    "female_designation": "Female Designation",
  #    "female_scale_of_pay": "Female Scale of Pay",
  #    "female_start_of_appointment": "Female Start of Appointment",
	 # "female_end_of_appointment": "Female End of Appointment",
  #    }

class AadhaarLookup(Form):
	aadhaar_number = forms.IntegerField(widget = forms.TextInput(attrs={'class': 'input-lg', 
		'type': 'text','placeholder': 'Aadhaar Number'}), label='Aadhaar Number')

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
