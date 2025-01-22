from rest_framework import serializers
from modules.car.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'status', 'photo_id')