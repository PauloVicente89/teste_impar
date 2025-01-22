from .models import Car
from typing import List, Optional
from modules.photo.models import Photo

class CarService:
    
    @staticmethod
    def get_all_cars(name: Optional[str] = None) -> List[Car]:
        queryset = Car.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    @staticmethod
    def get_car_by_id(id: str) -> Car:
        return Car.objects.filter(id=id).first()

    @staticmethod
    def create_car(name: str, photo: Photo | str) -> Car:
        return Car.objects.create(name=name, photo_id=photo)

    @staticmethod
    def delete_car(car_id: int) -> None:
        car = Car.objects.filter(id=car_id).select_related("photo_id").first()
        car.delete()
