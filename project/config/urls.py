from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api/cars/', include('modules.car.urls')),
    path('api/photo/', include('modules.photo.urls')),
    path('api/auth/', include('modules.authentication.urls')),
]
