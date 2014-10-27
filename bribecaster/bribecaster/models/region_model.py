from django.db import models

""" Model Representing a region
aggregate_speed_rating - int
aggregate_quality_rating - int
aggregate_cost_rating - int 

has_many offices

"""
class Region(models.Model):
	aggregate_cost_rating = models.IntField()
	aggregate_quality_rating = models.IntField()
	aggregate_speed_rating = models.IntField()

