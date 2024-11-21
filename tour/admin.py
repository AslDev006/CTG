from django.contrib import admin

from .models import TourModel
from django.utils.safestring import mark_safe

@admin.register(TourModel)
class NewsAdmin(admin.ModelAdmin):    
    list_display = ('id', 'title', 'image_tag')
    search_fields = ('title'),
    readonly_fields = ('update_time', 'active_time')
    ordering = ('title',)
    def image_tag(self, obj):
            if obj.photo:
                return mark_safe(f'<img src="{obj.photo.url}" style="width: 60px; height: 80px;" />')
            return "No Image"
        
    image_tag.short_description = 'City Photo'      