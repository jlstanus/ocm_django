from django.contrib.gis.db import models
from django.utils import timezone

class Scan(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, 
							verbose_name="Scan definition Date")
	station = models.ForeignKey('stations.Station', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "scan"
		ordering = ['date']
		verbose_name_plural = 'scans'

	def __str__(self):
		return self.name
