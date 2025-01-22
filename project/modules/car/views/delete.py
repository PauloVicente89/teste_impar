from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.car.services import CarService

class DeleteCarsView(APIView):
    def delete(self, request, car_id: int):
        CarService.delete_car(car_id=car_id)
        return Response(status=status.HTTP_204_NO_CONTENT)