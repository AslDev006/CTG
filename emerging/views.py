from django.shortcuts import render
from .serializers import  AutoCompleteSerializer, HotelDataSearchSerializer, RegionSearchEngineResultsPageSerializer, HotelSearchEngineResultsPageSerializer, OrderBookingFormSerializer, CreditCardDataTokenizationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
import requests
import json
from decouple import config

class AutoRegionSearchAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=AutoCompleteSerializer
    permission_classes=[AllowAny]
   
    def post(self, request):

        try:
            payload = json.dumps(request.data)
            headers = {
                    'Content-Type': 'application/json'
                }
            region_id_response=requests.request("POST", config('AUTOCOMPLETE_URL'), 
                                                headers=headers, 
                                                auth=(config('HOTEL_KEY_ID'),config('HOTEL_KEY_TOKEN_TEST')),
                                data=payload)
            region_id_list=region_id_response.json()
            return Response(region_id_list)
        except Exception:
            return Response(data=region_id_list['error'],status=region_id_response.status_code)
        

class HotelDataSearchAPIView(generics.GenericAPIView):
    queryset = None
    serializer_class = HotelDataSearchSerializer
    permission_classes = [AllowAny]
   
    def post(self, request):
        region_id_list = {}
        try:
            payload =json.dumps(request.data)
            headers = {
                'Content-Type': 'application/json'
            }
            hotel_id_response = requests.request("POST", config('HotelDataSearchURL'), 
                                                 headers=headers, 
                                                 auth=(config('HOTEL_KEY_ID'), config('HOTEL_KEY_TOKEN_TEST')),
                                                 data=payload)
            region_id_list = hotel_id_response.json()  
            return Response(region_id_list)
        except requests.exceptions.HTTPError as http_err:
            return Response(data={"error": str(http_err)}, status=hotel_id_response.status_code)
        except json.JSONDecodeError as json_err:
            return Response(data={"error": f"Invalid JSON response {json_err}"}, status=500)
        except Exception as e:
            return Response(data={"error": str(e)}, status=500)
        


class RegionSearchEngineResultsPageView(generics.GenericAPIView):
    queryset = None
    serializer_class = RegionSearchEngineResultsPageSerializer
    permission_classes = [AllowAny]
   
    def post(self, request):
        region_id_list = {}
        try:
            payload =json.dumps(request.data)
            headers = {
                'Content-Type': 'application/json'
            }
            hotel_id_response = requests.request("POST", config('RegionSearchEngineResultsURL'), 
                                                 headers=headers, 
                                                 auth=(config('HOTEL_KEY_ID'), config('HOTEL_KEY_TOKEN_TEST')),
                                                 data=payload)
            region_id_list = hotel_id_response.json()  
            return Response(region_id_list)
        except requests.exceptions.HTTPError as http_err:
            return Response(data={"error": str(http_err)}, status=hotel_id_response.status_code)
        except json.JSONDecodeError as json_err:
            return Response(data={"error": f"Invalid JSON response {json_err}"}, status=500)
        except Exception as e:
            return Response(data={"error": str(e)}, status=500)
        


class HotelSearchEngineResultsPageView(generics.GenericAPIView):
    queryset = None
    serializer_class = HotelSearchEngineResultsPageSerializer
    permission_classes = [AllowAny]
   
    def post(self, request):
        region_id_list = {}
        try:
            payload =json.dumps(request.data)
            headers = {
                'Content-Type': 'application/json'
            }
            hotel_id_response = requests.request("POST", config('HotelSearchEngineResultsURL'), 
                                                 headers=headers, 
                                                 auth=(config('HOTEL_KEY_ID'), config('HOTEL_KEY_TOKEN_TEST')),
                                                 data=payload)
            region_id_list = hotel_id_response.json()  
            return Response(region_id_list)
        except requests.exceptions.HTTPError as http_err:
            return Response(data={"error": str(http_err)}, status=hotel_id_response.status_code)
        except json.JSONDecodeError as json_err:
            return Response(data={"error": f"Invalid JSON response {json_err}"}, status=500)
        except Exception as e:
            return Response(data={"error": str(e)}, status=500)
        


class OrderBookingFormVIEW(generics.GenericAPIView):
    queryset = None
    serializer_class = OrderBookingFormSerializer
    permission_classes = [AllowAny]
   
    def post(self, request):
        region_id_list = {}
        try:
            payload =json.dumps(request.data)
            headers = {
                'Content-Type': 'application/json'
            }
            hotel_id_response = requests.request("POST", config('OrderBookingFormURL'), 
                                                 headers=headers, 
                                                 auth=(config('HOTEL_KEY_ID'), config('HOTEL_KEY_TOKEN_TEST')),
                                                 data=payload)
            region_id_list = hotel_id_response.json()  
            return Response(region_id_list)
        except requests.exceptions.HTTPError as http_err:
            return Response(data={"error": str(http_err)}, status=hotel_id_response.status_code)
        except json.JSONDecodeError as json_err:
            return Response(data={"error": f"Invalid JSON response {json_err}"}, status=500)
        except Exception as e:
            return Response(data={"error": str(e)}, status=500)




class CreditCardDataTokenizationView(generics.GenericAPIView):
    queryset = None
    serializer_class = CreditCardDataTokenizationSerializer
    permission_classes = [AllowAny]
   
    def post(self, request):
        region_id_list = {}
        try:
            payload =json.dumps(request.data)
            headers = {
                'Content-Type': 'application/json'
            }
            hotel_id_response = requests.request("POST", config('CreditCardDataTokenizationUrl'), 
                                                 headers=headers, 
                                                 auth=(config('HOTEL_KEY_ID'), config('HOTEL_KEY_TOKEN_TEST')),
                                                 data=payload)
            region_id_list = hotel_id_response.json()  
            return Response(region_id_list)
        except requests.exceptions.HTTPError as http_err:
            return Response(data={"error": str(http_err)}, status=hotel_id_response.status_code)
        except json.JSONDecodeError as json_err:
            return Response(data={"error": f"Invalid JSON response {json_err}"}, status=500)
        except Exception as e:
            return Response(data={"error": str(e)}, status=500)