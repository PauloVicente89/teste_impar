from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.car.services import CarService
from rest_framework.permissions import IsAdminUser

class DeleteCarsView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, car_id: int):
        CarService.delete_car(car_id=car_id)
        return Response(status=status.HTTP_204_NO_CONTENT)