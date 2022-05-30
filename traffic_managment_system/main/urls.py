from django.urls import path
from main import views


app_name = 'main'


urlpatterns = [
    path('car/', views.VehicleView.as_view(), name='car-list'),
    path('car/status/', views.VehicleStatusView.as_view(), name='car-status'),
    path('owner/', views.OwnerView.as_view(), name='owner-list'),
]
