from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Place
# Create your views here.

class home(TemplateView):
	template_name = 'geolocalisation/index.html'

class PlaceListView(ListView):

	model = Place
	paginate_by = 15  # if pagination is desired

def places_dataset(request):
	places = serialize('geojson', Place.objects.all())
	return HttpResponse(places, content_type='json')
