from django.urls import path, include
from .views import MapView, places_dataset, PlaceListView, PlaceCreateView, PlaceView, PlaceUpdate, PlaceDelete

urlpatterns = [
	path('map', MapView.as_view(), name='map'),
	path('<int:pk>/', PlaceView.as_view(), name='place'),
	path('places', places_dataset, name='places'),
	path('list', PlaceListView.as_view(), name='places_list'),
	path('create', PlaceCreateView.as_view(), name='place_create'),
	path('update/<int:pk>/', PlaceUpdate.as_view(), name='place_update'),
	path('delete/<int:pk>/', PlaceDelete.as_view(), name='place_delete'),
]