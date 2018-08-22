from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Place
# Create your views here.

class home(TemplateView):
	template_name = 'geolocalisation/index.html'

def places_dataset(request):
	places = serialize('geojson', Place.objects.all())
	return HttpResponse(places, content_type='json')
