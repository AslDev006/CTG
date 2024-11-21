from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import AboutModel
from .serializers import AboutSerializres


class AboutListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        about_objects = AboutModel.objects.all()
        serializer = AboutSerializres(about_objects, many=True)
        return Response(serializer.data)