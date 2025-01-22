from django.http import JsonResponse
from rest_framework.views import APIView
from modules.photo.services import get_photo_by_id

class RenderPhotoView(APIView):
    def get(self, request, photo_id: str):
        photo = get_photo_by_id(photo_id)
        return JsonResponse({'base64': photo.base64})
