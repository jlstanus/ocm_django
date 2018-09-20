from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.serializers import serialize
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from .models import Place
from .forms import PlaceForm
# Create your views here.

class MapView(TemplateView):
	template_name = 'geolocalisation/map.html'

class PlaceView(DetailView):
	context_object_name = "place"
	model = Place
	template_name = 'geolocalisation/place_detail.html'
		
class PlaceListView(ListView):
	model = Place
	paginate_by = 9  # if pagination is desired

class PlaceCreateView(CreateView):
	model = Place
	form_class = PlaceForm

	def get_success_url(self):
		return reverse('stations_from_list', args=(self.object.pk,))

class PlaceUpdate(UpdateView):
	model = Place
	template_name = 'geolocalisation/place_form.html'
	form_class = PlaceForm

	def get_success_url(self):
		return reverse('place', args=(self.object.pk,))

class PlaceDelete(DeleteView):
	model = Place
	template_name = 'geolocalisation/place_delete.html'
	# success_url = 'liste'
	def get_success_url(self):
		return reverse('places_list')

def places_dataset(request):
	places = serialize('geojson', Place.objects.all())
	return HttpResponse(places, content_type='json')
