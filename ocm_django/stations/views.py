from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from .models import Station
from geolocalisation.models import Place
from .forms import StationForm
# Create your views here.

class StationView(DetailView):
	context_object_name = "station"
	model = Station
	template_name = 'stations/station_detail.html'
		
class StationListView(ListView):

	model = Station
	paginate_by = 9  # if pagination is desired
		
class StationCreateView(CreateView):
	model = Station
	form_class = StationForm

	def get_success_url(self):
		return reverse('station', args=(self.object.pk,))

class StationUpdate(UpdateView):
	model = Station
	template_name = 'stations/station_form.html'
	form_class = StationForm

	def get_success_url(self):
		return reverse('station', args=(self.object.pk,))

class StationDelete(DeleteView):
	model = Station
	template_name = 'stations/station_delete.html'
	# success_url = 'liste'
	def get_success_url(self):
		return reverse('stations_list')

class StationListViewFromPlace(ListView):
	model = Station
	paginate_by = 9
	template_name = "station_list.html"

	def get_queryset(self):
		del self.request.session['station_name']
		self.request.session['place_name'] = Place.objects.get(id=self.kwargs['pk']).name
		self.request.session['place_id'] = self.kwargs['pk']
		return Station.objects.filter(place__id=self.kwargs['pk'])

