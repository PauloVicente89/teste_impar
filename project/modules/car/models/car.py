from django.db import models
from modules.photo.models import Photo
import uuid

class Car(models.Model):
    class Status(models.TextChoices):
        SOLD = "SOLD", "Vendido"
        AVAILABLE = "AVAILABLE", "Disponível"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=40, db_index=True)
    status: str = models.CharField(choices=Status.choices, default="AVAILABLE", db_index=True)

    class Meta:
        db_table = "cars"
        