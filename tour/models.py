from django.db import models
import uuid
from ckeditor.fields import RichTextField

class TourModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to='media_tour/')
    description = RichTextField()
    title = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)       
    active_time = models.DateTimeField(null=True, blank=True)