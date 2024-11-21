from rest_framework import generics
from .models import TourModel
from .serializers import TourModelSerializer

class TourModelList(generics.ListCreateAPIView):
    queryset = TourModel.objects.all()  
    serializer_class = TourModelSerializer  

class TourModelDetail(generics.RetrieveAPIView):
    queryset = TourModel.objects.all()  
    serializer_class = TourModelSerializer 