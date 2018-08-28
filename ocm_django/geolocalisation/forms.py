from django import forms
from .models import Place
from leaflet.forms.fields import PointField

class PlaceForm(forms.ModelForm):
	name = forms.CharField(max_length=100, help_text="Scan project name", required=True)
	location = PointField()
	description = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Place
		fields = ('name', 'location', 'description')