from django.contrib.gis.db import models
from django.utils import timezone

class Place(models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	description = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, 
							verbose_name="Place definition Date")
	class Meta:
		verbose_name = "Place"
		ordering = ['date']
		verbose_name_plural = 'places'

	def __str__(self):
		return self.name
