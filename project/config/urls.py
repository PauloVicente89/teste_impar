from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from config.swagger import general_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', general_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

    # API routes
    path('api/cars/', include('modules.car.urls')),
    path('api/photo/', include('modules.photo.urls')),
    path('api/auth/', include('modules.authentication.urls')),
]
