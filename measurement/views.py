# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SensorSerializer, SensorDetailSerializer 
from .models import Sensor, Measurement
from rest_framework import status



class AllSensorView(APIView):

    def get(self, request):
        queryset = Sensor.objects.all()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorView(APIView):  

    def get(self, request, pk):
        queryset = Sensor.objects.filter(pk=pk)
        serializer = SensorDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=int(pk))
        except Sensor.DoesNotExist:
            sensor = None
        if sensor:
            description = request.GET.get('description', sensor.description)
            name = request.GET.get('name', sensor.name)
            sensor.description=description
            sensor.name=name
            sensor.save()
            response = sensor.__dict__
            response.pop('_state')
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'status': 'Sensor does not exist'},
                    status=status.HTTP_400_BAD_REQUEST
                    )


class MeasurementView(APIView):

    def post(self, request):
        try:
            sensor_id = int(request.headers.get('sensor'))
            sensor = Sensor.objects.get(id=sensor_id)
            temperatute = int(request.headers.get('temperature'))
        except TypeError:
            return Response(
                    {'status': 'Temperatute and id must be integer'},
                    status=status.HTTP_400_BAD_REQUEST
                    )
        photo = request.data['photo']
        photo.name = f'{sensor_id}-{datetime.datetime.utcnow()}.jpeg'
        measurement = Measurement(sensor=sensor, temperature=temperatute, photo=photo)
        measurement.save()
        response = measurement.__dict__
        response.pop('_state')
        return Response(response, status=status.HTTP_200_OK)
