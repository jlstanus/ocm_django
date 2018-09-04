from django.contrib import admin
from .models import Station
# Register your models here.


class StationAdmin(admin.ModelAdmin):
	list_display = ('name','description','date','place')
	list_filter = ('name','date')
	date_hierarchy = 'date'
	ordering = ('date', )
	search_fields = ('name', 'date', 'description')

admin.site.register(Station, StationAdmin)