# from typing import List
# from uuid import UUID
# from car.serializers import CarSerializer
# from car.models import Car

# class CarService:

#     @staticmethod
#     def create_car(name: str, status: str, photo_base64: str) -> Car:
#         photo = Photo.objects.create(base64=photo_base64)
#         car = Car.objects.create(name=name, status=status, photo_id=photo)
#         return car

#     @staticmethod
#     def update_car(car_id: UUID, name: str, status: str, photo_base64: str) -> Car:
#         car = Car.objects.get(id=car_id)
#         car.name = name
#         car.status = status
#         photo = Photo.objects.create(base64=photo_base64)
#         car.photo_id = photo
#         car.save()
#         return car

#     @staticmethod
#     def delete_car(car_id: UUID) -> None:
#         car = Car.objects.get(id=car_id)
#         car.delete()

#     @staticmethod
#     def get_cars(name: str = None, status: str = None) -> List[Car]:
#         query = Car.objects.all()
#         if name:
#             query = query.filter(name__icontains=name)
#         if status:
#             query = query.filter(status__icontains=status)
#         return query

#     @staticmethod
#     def get_car_by_id(car_id: UUID) -> Car:
#         return Car.objects.get(id=car_id)
