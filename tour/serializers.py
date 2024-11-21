from rest_framework import serializers
from .models import TourModel

class TourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourModel
        fields = '__all__'