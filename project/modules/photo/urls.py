from django.urls import path
from modules.photo.views import CreatePhotoView

urlpatterns = [
    path('create/', CreatePhotoView.as_view()),
]
