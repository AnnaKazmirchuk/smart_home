from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView, \
    ListAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# создание датчика
class CreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def create_sensor(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        Sensor(name=name, description=description).save()
        return Response({'status': 'Датчик добавлен'})


# получение датчиков
class SensorsListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# обновление датчика
class ChangeSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# добавление измерения
class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create_measurement(self, request):
        sensor = request.POST.get('sensor')
        temperature = request.POST.get('temperature')
        MeasurementSerializer(sensor=sensor, temperature=temperature).save()
        return Response({'status': 'Измерение добавлено'})


# получение информации по датчику
class SensorDetailsView(RetrieveAPIView):
    queryset = Sensor.objects.all().prefetch_related('sensor')
    serializer_class = SensorDetailSerializer