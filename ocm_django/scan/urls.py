from django.urls import path

from .views import ScanListView, ScanCreateView, ScanView, ScanUpdate, ScanDelete

urlpatterns = [
	path('<int:pk>/', ScanView.as_view(), name='scan'),
	path('list', ScanListView.as_view(), name='scans_list'),
	path('create', ScanCreateView.as_view(), name='scan_create'),
	path('update/<int:pk>/', ScanUpdate.as_view(), name='scan_update'),
	path('delete/<int:pk>/', ScanDelete.as_view(), name='scan_delete'),
]