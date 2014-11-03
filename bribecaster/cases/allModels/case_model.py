from django.db import models

""" A Case Model containing the forms and followups from a particular citizen visit to an office.

belongs to a user
belongs to an office
"""
class Case(models.Model):
	#customer_information
	
	sms_selected = models.BooleanField()
	robo_call_selected = models.BooleanField()
	follow_up_selected = models.BooleanField()

	sms_response = models.ManyToMany(SMSResponse)
	robo_response = models.ForeignKey(RoboResponse)
	call_response = models.ManyToMany(CallResponse)

	citizen = models.ForeignKey(Citizen)
	office = models.ForeignKey(Office)
	user = models.ManyToMany(User)


