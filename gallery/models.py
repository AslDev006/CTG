from django.db import models
import uuid
class GalleryModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255)