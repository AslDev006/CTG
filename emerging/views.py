from django.shortcuts import render
from .serializers import RegionSearchEngineResultsPageSerializer, AutoCompleteSerializer, HotelSearchEngineResultsPageSerialzier
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
            payload = json.dumps({
                    "query": request.data['region_name'],
                    "language": request.data['language']
                })
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
        




class RegionSearchEngineResultsPageView(generics.GenericAPIView):
    queryset=None
    serializer_class=RegionSearchEngineResultsPageSerializer
    permission_classes=[AllowAny]
   
    def post(self, request):
        try:
            guest_data = request.data['guests'][0]
            children_ages = [child['age'] for child in guest_data.get('children', [])]
            payload = {
                "checkin": request.data['checkin'],
                "checkout": request.data['checkout'],
                "residency": request.data['residency'],
                "language": request.data['language'],
                "guests": [{
                    "adults": guest_data['adults'],
                    "children": children_ages  
                }],
                "region_id": request.data['region_id'],
                "currency": request.data['currency']
            }

            headers = {
                'Content-Type': 'application/json'
            }

            region_list_response = requests.post(config('RegionSearchEngineResultsURL'), 
                headers=headers, 
                auth=(config('HOTEL_KEY_ID'), config('HOTEL_KEY_TOKEN_TEST')),
                json=payload  
            )
            
            region_list_response.raise_for_status()  
            region_id_list = region_list_response.json()
            return Response(region_id_list)

        except requests.exceptions.HTTPError as http_err:
            return Response(data={"error": str(http_err)}, status=region_list_response.status_code)
        except json.JSONDecodeError as json_err:
            return Response(data={"error": "Invalid JSON response"}, status=500)
        except Exception as e:
            return Response(data={"error": str(e)}, status=500)
        



class HotelSearchEngineResultsPageView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelSearchEngineResultsPageSerialzier
    permission_classes=[AllowAny]
    def post(self, request):
        try:
            guest_data = request.data['guests'][0]
            children_ages = [child['age'] for child in guest_data.get('children', [])]
            ids_name = [hotel['name'] for hotel in request.data['ids']]

            payload = {
                "ids": ids_name,
                "checkin": request.data['checkin'],
                "checkout": request.data['checkout'],
                "residency": request.data.get('residency'),
                "language": request.data.get('language'),
                "guests": [{
                    "adults": guest_data['adults'],
                    "children": children_ages  
                }],
                "currency": request.data.get('currency')
            }

            print("Payload being sent:", payload)  # Debugging line

            headers = {
                'Content-Type': 'application/json'
            }

            hotel_list_response = requests.post(
                config('HotelSearchEngineResultsURL'),
                headers=headers,
                auth=(config('HOTEL_KEY_ID'), config('HOTEL_KEY_TOKEN_TEST')),
                json=payload  
            )
            
            hotel_list_response.raise_for_status()
            region_id_list = hotel_list_response.json()
            return Response(region_id_list)

        except requests.exceptions.HTTPError as http_err:
            error_details = hotel_list_response.json() if hotel_list_response.content else {}
            return Response(data={"error": str(http_err), "details": error_details}, status=hotel_list_response.status_code)
        except json.JSONDecodeError as json_err:
            return Response(data={"error": "Invalid JSON response"}, status=500)
        except Exception as e:
            return Response(data={"error": str(e)}, status=500)