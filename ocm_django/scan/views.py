from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from stations.models import Station
from .models import Scan
from .forms import ScanForm
from . import plots
# Create your views here.

class ScanView(DetailView):
	context_object_name = "scan"
	model = Scan
	template_name = 'scan/scan_detail.html'
		
class ScanListView(ListView):
	model = Scan
	paginate_by = 9  # if pagination is desired

class ScanCreateView(CreateView):
	model = Scan
	form_class = ScanForm

	def get_success_url(self):
		return reverse('scan', args=(self.object.pk,))

class ScanUpdate(UpdateView):
	model = Scan
	template_name = 'scan/scan_form.html'
	form_class = ScanForm

	def get_success_url(self):
		return reverse('scan', args=(self.object.pk,))

class ScanDelete(DeleteView):
	model = Scan
	template_name = 'scan/scan_delete.html'
	# success_url = 'liste'
	def get_success_url(self):
		return reverse('scan_list')

class ScanListViewFromStation(ListView):
	model = Scan
	paginate_by = 9
	template_name = "scan_list.html"

	def get_queryset(self):
		self.request.session['station_name'] = Station.objects.get(id=self.kwargs['pk']).name
		self.request.session['station_id'] = self.kwargs['pk']
		return Scan.objects.filter(station__id=self.kwargs['pk'])

class Plot3DScatterView(TemplateView):
    template_name = "scan/scan_plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot3DScatterView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot3D_scatter
        return context


