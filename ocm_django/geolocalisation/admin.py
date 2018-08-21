from django.contrib import admin
from .models import Place
# Register your models here.
from leaflet.admin import LeafletGeoAdmin

class PlaceAdmin(LeafletGeoAdmin):
	list_display = ('name','date','location')
	list_filter = ('name','date')
	date_hierarchy = 'date'
	ordering = ('date', )
	search_fields = ('name', 'date')

admin.site.register(Place, PlaceAdmin)