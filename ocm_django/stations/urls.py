from django.urls import path

from .views import StationListView, StationCreateView, StationView, StationUpdate, StationDelete, StationListViewFromPlace

urlpatterns = [
	path('<int:pk>/', StationView.as_view(), name='station'),
	path('list', StationListView.as_view(), name='stations_list'),
	path('create', StationCreateView.as_view(), name='station_create'),
	path('create/<int:pk/', StationCreateView.as_view(), name='station_create_from_station'),
	path('update/<int:pk>/', StationUpdate.as_view(), name='station_update'),
	path('delete/<int:pk>/', StationDelete.as_view(), name='station_delete'),
	path('list/<int:pk>/', StationListViewFromPlace.as_view(), name='stations_from_list' )
]