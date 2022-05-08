from django.urls import path

from measurement.views import CreateSensorView, ChangeSensorView, CreateMeasurementView, SensorDetailsView, \
    SensorsListView

urlpatterns = [
    path('sensors/create/', CreateSensorView.as_view()),
    path('sensors/update/<pk>/', ChangeSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('sensors/', SensorsListView.as_view()),
    path('sensors/details/<pk>/', SensorDetailsView.as_view()),
]
