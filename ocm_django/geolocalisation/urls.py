from django.urls import path
from .views import home, places_dataset, PlaceListView

urlpatterns = [
	path('', home.as_view(), name='home'),
	path('places', places_dataset, name='places'),
	path('list', PlaceListView.as_view(), name='places_list'),
]