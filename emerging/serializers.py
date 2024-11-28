from rest_framework import serializers
from datetime import datetime, timedelta

class AutoCompleteSerializer(serializers.Serializer):
    region_name = serializers.CharField(required=True)
    language = serializers.CharField(required=False)

class ChildrenDataSerializers(serializers.Serializer):
    age = serializers.IntegerField()

class HotelIDDataSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

class GuestDataSerializers(serializers.Serializer):
    adults = serializers.IntegerField(required=True)
    children = serializers.ListField(child=ChildrenDataSerializers(), required=False)


class EarlyCheckinDataSerializer(serializers.Serializer):
    time = serializers.DateTimeField(required=False)

class LateCheckoutDataSerializer(serializers.Serializer):
    time = serializers.DateTimeField(required=False)

class UpsellDataSerializer(serializers.Serializer):
    early_checkin = serializers.ListField(child=EarlyCheckinDataSerializer(), required=False)
    late_checkout = serializers.ListField(child=LateCheckoutDataSerializer(), required=False)
    only_eclc = serializers.BooleanField(required=False)

class RegionSearchEngineResultsPageSerializer(serializers.Serializer):
    region_id = serializers.IntegerField(required=True)
    checkin = serializers.DateField(required=True)
    checkout = serializers.DateField(required=True)
    guests = serializers.ListField(child=GuestDataSerializers(), required=True)
    currency = serializers.CharField(required=False)
    residency = serializers.CharField(required=False)
    hotels_limit = serializers.IntegerField(required=False)
    timeout = serializers.IntegerField(required=False, max_value=100)
    upsells = serializers.ListField(child=UpsellDataSerializer(), required=False)
    language = serializers.CharField(required=False)


class HotelSearchEngineResultsPageSerialzier(serializers.Serializer):
    ids = serializers.ListField(child=HotelIDDataSerializer(), required=True, )
    checkin = serializers.DateField(required=True)
    checkout = serializers.DateField(required=True)
    guests = serializers.ListField(child=GuestDataSerializers(), required=True)
    currency = serializers.CharField(required=False)
    residency = serializers.CharField(required=False)
    hotels_limit = serializers.IntegerField(required=False)
    timeout = serializers.IntegerField(required=False, max_value=100)
    upsells = serializers.ListField(child=UpsellDataSerializer(), required=False)
    language = serializers.CharField(required=False)