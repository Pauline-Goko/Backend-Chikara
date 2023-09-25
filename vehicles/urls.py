from django.urls import path
from .views import VehicleList, VehicleDetail

urlpatterns = [
    path('vehicles/', VehicleList.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
]
