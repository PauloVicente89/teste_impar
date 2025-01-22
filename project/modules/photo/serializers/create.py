from rest_framework import serializers
from modules.photo.models import Photo

class CreatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'Base64',
        ]
        
    def create(self, validated_data):
        return Photo.objects.create(**validated_data)