from django.urls import path
from .views import TourModelList, TourModelDetail

urlpatterns = [
    path('', TourModelList.as_view(), name='tour-list'),  
    path('<uuid:pk>/', TourModelDetail.as_view(), name='tour-detail'),  
]