from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def select_gps(request):
	return render(request, 'gps/index.html', {})

def read_gps(request):
	gps_name = 'bt747'
	return render(request, "gps/gps.html", {
		'gps_name_json': mark_safe(json.dumps(gps_name)),
		'sensor' : gps_name,
})