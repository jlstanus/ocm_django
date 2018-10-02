from django.urls import path
from .views import read_gps, select_gps

urlpatterns = [
	path('select_gps/', select_gps, name='select_gps' ),
    path('bt747/', read_gps, name='read_gps'),
]