from rest_framework import serializers
from modules.photo.models import Photo

class GetPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id',
            'base64',
        ]
        
    def get(self):
        return Photo.objects.all().order_by("id")