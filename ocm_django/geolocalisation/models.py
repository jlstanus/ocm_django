from django.db import models
from django.utils import timezone

class Place(models.Model):
	name = models.CharField(max_length=20)
	localisation = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, 
							verbose_name="Place definition Date")
	class Meta:
		verbose_name = "Place"
		ordering = ['date']

	def __str__(self):
		return self.name