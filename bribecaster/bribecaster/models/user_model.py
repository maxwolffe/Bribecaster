from django.db import models

""" A User Model representing an employee of the government. 


"""
class User(model.Models):
	first_name = models.CharField(max_length = 40)
	last_name = models.CharField(max_length = 40)
	employee_number = models.IntField()

	case = models.ManyToManyField(Case)
	office = models.ForeignKey(Office)

