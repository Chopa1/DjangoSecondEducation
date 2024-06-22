# inventory/urls.py
from django.urls import path
from .views import (
    ManufacturerListView,
    ManufacturerDetailView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView
)

urlpatterns = [
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    path('manufacturers/new/', ManufacturerCreateView.as_view(), name='manufacturer-create'),
    path('manufacturers/<int:pk>/edit/', ManufacturerUpdateView.as_view(), name='manufacturer-update'),
    path('manufacturers/<int:pk>/delete/', ManufacturerDeleteView.as_view(), name='manufacturer-delete'),
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/new/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/edit/', CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
]
