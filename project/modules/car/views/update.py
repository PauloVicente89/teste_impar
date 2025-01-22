from rest_framework.response import Response
from rest_framework import status
from modules.car.services import CarService
from modules.car.serializers import CarSerializer, UpdateCarSerializer
from modules.car.utils import photo_validation
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

class UpdateCarsView(APIView):
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]

    def get_object(self, car_id: str):
        return CarService.get_car_by_id(car_id)

    def put(self, request, car_id,*args, **kwargs):
        car = self.get_object(car_id)
        if not car:
            return Response({"error": "ID inválido"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        photo_file = data.get('photo')
        if photo_file:
            new_photo = photo_validation(photo_file)
            data['photo_id'] = new_photo.id

        serializer = UpdateCarSerializer(
            car,
            data=data, 
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)