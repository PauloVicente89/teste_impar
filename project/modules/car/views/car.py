from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.car.services import CarService
from modules.photo.services import get_photo_by_id
from modules.car.serializers import CarSerializer
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse

class CarView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        cars = CarService.get_all_cars(name=name)
        paginator = PageNumberPagination()
        paginated_cars = paginator.paginate_queryset(cars, request)
        serializer = CarSerializer(paginated_cars, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        data = request.data
        car = CarService.create_car(
            name=data['name'],
            status=data['status'],
            photo_id=data['photo_id']
        )
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, car_id: int):
        """Edita um carro."""
        data = request.data
        car = CarService.update_car(
            car_id=car_id,
            name=data['name'],
            status=data['status'],
            photo_id=data['photo_id']
        )
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def delete(self, request, car_id: int):
        """Exclui um carro."""
        CarService.delete_car(car_id=car_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RenderPhotoView(APIView):
    def get(self, request, photo_id: int):
        """Renderiza a foto pelo ID."""
        photo = get_photo_by_id(photo_id)
        return JsonResponse({'base64': photo.base64})
