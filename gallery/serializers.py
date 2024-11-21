from rest_framework import serializers
from .models import GalleryModels



class GallerySerializres(serializers.ModelSerializer):
    class Meta:
        model = GalleryModels
        fields = '__all__'