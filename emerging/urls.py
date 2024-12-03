from django.urls import path
from .views import AutoRegionSearchAPIView, HotelDataSearchAPIView, RegionSearchEngineResultsPageView, HotelSearchEngineResultsPageView, OrderBookingFormVIEW, CreditCardDataTokenizationView

urlpatterns = [
    path('auto-search/', AutoRegionSearchAPIView.as_view(), name='auto-search'),
    path('region-search/', RegionSearchEngineResultsPageView.as_view(), name='auto-search'),
    path('hotel-search/', HotelSearchEngineResultsPageView.as_view(), name='hotel-search'),
    path('hotel-data-search/', HotelDataSearchAPIView.as_view(), name='hotel-data-search'),
    path('order-booking/', OrderBookingFormVIEW.as_view(), name='order-booking'),
    path('credit-tokenization/', CreditCardDataTokenizationView.as_view(), name='credit-tokenization'),
]