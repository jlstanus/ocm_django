from django.contrib import admin
from .models import Scan
# Register your models here.


class ScanAdmin(admin.ModelAdmin):
	list_display = ('name','description','date','station')
	list_filter = ('name','date')
	date_hierarchy = 'date'
	ordering = ('date', )
	search_fields = ('name', 'date', 'description')

admin.site.register(Scan, ScanAdmin)