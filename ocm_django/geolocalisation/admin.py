from django.contrib import admin
from .models import Place
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('name','date','localisation')
	list_filter = ('name','date')
	date_hierarchy = 'date'
	ordering = ('date', )
	search_fields = ('name', 'date')

admin.site.register(Place, PlaceAdmin)