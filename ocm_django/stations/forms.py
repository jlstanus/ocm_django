from django import forms
from .models import Station


class StationForm(forms.ModelForm):
	name = forms.CharField(max_length=100, help_text="Station name", required=True)
	description = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Station
		fields = ('name', 'description', 'place')