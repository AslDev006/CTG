from django.urls import path
from .views import AutoRegionSearchAPIView, RegionSearchEngineResultsPageView, HotelSearchEngineResultsPageView
urlpatterns = [
    path('auto-search/', AutoRegionSearchAPIView.as_view(), name='auto-search'),
    path('region-search/', RegionSearchEngineResultsPageView.as_view(), name='region-search'),
    path('hotel-search/', HotelSearchEngineResultsPageView.as_view(), name='hotel-search'),
]