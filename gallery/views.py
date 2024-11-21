from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import GalleryModels
from .serializers import GallerySerializres


class GalleryListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        about_objects = GalleryModels.objects.all()
        serializer = GallerySerializres(about_objects, many=True)
        return Response(serializer.data)