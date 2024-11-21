from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.safestring import mark_safe

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name','image_tag', 'email', 'is_staff', 'region', 'district')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'profile_photo', 'region', 'district')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'region', 'district', 'is_staff', 'is_active')
        }),
    )
    def image_tag(self, obj):
            if obj.profile_photo:
                return mark_safe(f'<img src="{obj.profile_photo.url}" style="width: 60px; height: 80px;" />')
            return "No Image"
        
    image_tag.short_description = 'Profile Photo'  
admin.site.register(CustomUser, CustomUserAdmin)