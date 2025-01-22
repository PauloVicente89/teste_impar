from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api/', include(router.urls)),
]
