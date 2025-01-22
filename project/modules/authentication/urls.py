from django.urls import path
from modules.authentication.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]
