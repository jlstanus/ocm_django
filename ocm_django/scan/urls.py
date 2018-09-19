from django.urls import path

from .views import ScanListView, ScanCreateView, ScanView, ScanUpdate, ScanDelete, ScanListViewFromStation, Plot3DScatterView

urlpatterns = [
	path('<int:pk>/', ScanView.as_view(), name='scan'),
	path('list', ScanListView.as_view(), name='scans_list'),
	path('create', ScanCreateView.as_view(), name='scan_create'),
	path('update/<int:pk>/', ScanUpdate.as_view(), name='scan_update'),
	path('delete/<int:pk>/', ScanDelete.as_view(), name='scan_delete'),
	path('plot3d_scatter/', Plot3DScatterView.as_view(), name='plot3d_scatter'),
	path('list/<int:pk>/', ScanListViewFromStation.as_view(), name='scans_from_list')
]