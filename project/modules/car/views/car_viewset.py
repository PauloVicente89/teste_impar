from rest_framework import viewsets
from modules.car.models import Car
from modules.car.serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().select_related("photo_id")
    serializer_class = CarSerializer
