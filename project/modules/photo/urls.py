from django.urls import path
from modules.photo.views import RenderPhotoView

urlpatterns = [
    path('view/<uuid:photo_id>/', RenderPhotoView.as_view()),
]
