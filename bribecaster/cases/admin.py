from django.contrib import admin
from cases.models import Citizen, Region, User, Office, Case, OfficeVisit, RoboCallFeedback, SMSFeedback, OBCForm

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Region)
admin.site.register(User)
admin.site.register(Office)
admin.site.register(Case)
admin.site.register(OfficeVisit)
admin.site.register(RoboCallFeedback)
admin.site.register(SMSFeedback)
admin.site.register(OBCForm)
