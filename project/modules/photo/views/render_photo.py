from django.http import JsonResponse
from rest_framework.views import APIView
from modules.photo.services import PhotoService

class RenderPhotoView(APIView):
    def get(self, request, photo_id: str) -> str:
        photo = PhotoService.get_photo_by_id(photo_id)
        return JsonResponse({'base64': photo.base64})
