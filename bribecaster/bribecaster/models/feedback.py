from django.db import models

RESPONSE_TYPE = (
    ('0', 'picked-up'),
    ('1', 'busy'),
    ('2', 'voicemail'),
    ('3', 'not-a-number'),
)

class Feedback(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	phone_number = models.IntegerField
	call_time = models.DateTimeField
	call_response = models.CharField(max_length=1, choices=RESPONSE_TYPE)
	sms_sent = models.CharField(max_length = 140)
	sms_response = models.CharField