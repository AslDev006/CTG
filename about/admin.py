from django.contrib import admin
from .models import AboutModel
# Register your models here.
@admin.register(AboutModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    