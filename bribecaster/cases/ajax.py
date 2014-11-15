from django.utils import json
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def lookup(request, text):
	dajax = Dajax()
	dajax.assign('#a_result','value', str(text))
	return dajax.json()