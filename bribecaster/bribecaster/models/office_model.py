from django.db import models

""" Represents an Office:
Has many cases, users (employees), 
Belongs to a region,


"""
class Office(models.Model):
	address = models.CharField(max_length = 30)
	phone_number = models.CharField(max_length = 20)
	office_head = models.CharField(max_length = 30) # Should maybe be a user
	speed_rating = models.IntField()
	cost_rating = models.IntField()
	quality_rating = models.IntField()
	cases = models.ManyToMany(Case)
	region = models.ForeignKey(Region)
