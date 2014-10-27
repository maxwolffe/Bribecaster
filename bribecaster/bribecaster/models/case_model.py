from django.db import models


class Case(models.Model):
	#customer_information
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 40)
	phone_number = models.CharField(max_length = 20)

	sms_selected = models.BooleanField()
	robo_call_selected = models.BooleanField()
	follow_up_selected = models.BooleanField()

	sms_response = models.ManyToMany(SMSResponse)
	robo_response = models.ForeignKey(RoboResponse)
	call_response = models.ManyToMany(CallResponse)

	user = models.ForiegnKey(User)
