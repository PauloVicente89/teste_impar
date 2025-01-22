from django.urls import path
from modules.car.views import (
    GetAllCarsView,
    CreateCarsView,
    UpdateCarsView,
    DeleteCarsView,
)

urlpatterns = [
    path('view/', GetAllCarsView.as_view()),
    path('create/', CreateCarsView.as_view()),
    path('update/<uuid:car_id>/', UpdateCarsView.as_view()),
    path('remove/<uuid:car_id>/', DeleteCarsView.as_view()), 
]
