from django.db import models
from ckeditor.fields import RichTextField
import uuid
class AboutModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = RichTextField()
    img = models.ImageField(upload_to='about_photos/')    
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)       
    active_time = models.DateTimeField(null=True, blank=True)