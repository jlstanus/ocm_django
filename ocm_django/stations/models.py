from django.contrib.gis.db import models
from django.utils import timezone

class Station(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, 
							verbose_name="Station definition Date")
	place = models.ForeignKey('geolocalisation.Place', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "station"
		ordering = ['date']
		verbose_name_plural = 'stations'

	def __str__(self):
		return self.name
