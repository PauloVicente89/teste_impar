from rest_framework.response import Response
from rest_framework import status, generics
from modules.car.services import CarService
from modules.car.serializers import CarSerializer
from config.pagination import CustomGeneralPagination

class GetAllCarsView(generics.ListAPIView):
    serializer_class = CarSerializer
    pagination_class = CustomGeneralPagination

    def get_queryset(self):
        name = self.request.query_params.get('name')
        return CarService.get_all_cars(name=name)