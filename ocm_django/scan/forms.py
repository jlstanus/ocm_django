from django import forms
from .models import Scan


class ScanForm(forms.ModelForm):
	name = forms.CharField(max_length=100, help_text="Scan name", required=True)
	description = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Scan
		fields = ('name', 'description', 'station')