from dangjo.db import models

""" A Citizen Model representing citizens who visit the office

has_many cases
belong_to region

"""
class Citizen(models.Model):
	first_name = models.CharField(max_length = 40)
	last_name = models.CharField(max_length = 40)
	phone_number = models.CharField(max_length = 20)
	address = models.CharField(max_length = 20)

	region = models.ForeignKey(Region)

