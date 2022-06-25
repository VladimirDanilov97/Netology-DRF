from django.urls import path
from . import views



urlpatterns = [
    path('sensors/', views.AllSensorView.as_view()),
    path('sensors/<pk>/', views.SensorView.as_view()),
    path('measurements/', views.MeasurementView.as_view())
]
