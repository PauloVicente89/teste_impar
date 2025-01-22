from drf_yasg.views import get_schema_view as swagger_schema_view
from drf_yasg import openapi
from rest_framework import permissions

api_info = openapi.Info(
    title="API - Teste seletivo ÍMPAR",
    default_version='v1.0',
    description="Documentação de API",
    contact=openapi.Contact(email="contato@impar.com.br"),
)
general_permission = (permissions.IsAdminUser,)
general_schema_view = swagger_schema_view(
    info=api_info,
    public = True,
    permission_classes=general_permission,
)