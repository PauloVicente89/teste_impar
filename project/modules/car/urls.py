from rest_framework.routers import DefaultRouter
from modules.car.views import CarViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)