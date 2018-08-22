from django.urls import path
from .views import home, places_dataset

urlpatterns = [
	path('', home.as_view(), name = 'home'),
	path('places', places_dataset, name = 'places'),
]