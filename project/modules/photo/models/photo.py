from django.db import models
import uuid

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    base64 = models.TextField()

    class Meta:
        db_table = "photos"