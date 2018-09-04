from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from .models import Scan
from .forms import ScanForm
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


