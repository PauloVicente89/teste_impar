from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from modules.photo.serializers import CreatePhotoSerializer

class CreatePhotoView(ModelViewSet):
    def post(self, request):
        try:
            serializer = CreatePhotoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"success": "Sua foto foi salva"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"error": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
        
