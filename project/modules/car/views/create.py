from rest_framework.response import Response
from rest_framework import status, generics
from modules.car.services import CarService
from modules.car.serializers import CarSerializer
from modules.car.utils import photo_validation
from rest_framework.permissions import IsAdminUser

class CreateCarsView(generics.ListAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]

    def post(self, request):
        data = request.data.copy()

        photo_file = data.get('photo')
        if photo_file:
            new_photo = photo_validation(photo_file)
            data['photo_id'] = new_photo

        car = CarService.create_car(
            name=data['name'],
            photo=data['photo_id'],
        )
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_201_CREATED)