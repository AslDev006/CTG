from rest_framework import serializers
from datetime import datetime, timedelta
import re

def validate_language(value):
    allowed_languages = [
        "ar", "bg", "cs", "de", "el", "en", "es", "fr", "he", "hu", 
        "it", "ja", "kk", "ko", "nl", "pl", "pt", "pt_PT", "ro", 
        "ru", "sq", "sr", "th", "tr", "uk", "vi", "zh_CN"
    ]
    if value not in allowed_languages:
        raise serializers.ValidationError(f"{value} is not a valid language code.")
    return value


class AutoCompleteSerializer(serializers.Serializer):
    query = serializers.CharField(required=True)
    language = serializers.CharField(validators=[validate_language],required=False)

class HotelDataSearchSerializer(serializers.Serializer):
    id = serializers.CharField(required=False, allow_null=True, help_text="The unique hotel identifier. Either this field or the hid field is required.")
    hid = serializers.IntegerField(required=False, allow_null=True, help_text="The most preferred hotel ID. Either this field or the id field is required.")
    language = serializers.CharField(validators=[validate_language], required=False, allow_null=True, help_text="The language")
    
    def validate(self, attrs):
        if not (attrs.get('id') or attrs.get('hid')):
            raise serializers.ValidationError("Either 'id' or 'hid' must be provided.")
        return attrs

class ChildSerializer(serializers.Serializer):
    age = serializers.IntegerField(required=True, min_value=0, max_value=17)  

class GuestSerializer(serializers.Serializer):
    adults = serializers.IntegerField(required=True, min_value=1, max_value=6)
    children = serializers.ListField(
        child=ChildSerializer(),
        required=False,
        max_length=4  
    )

class ECDataSerializer(serializers.Serializer):
    time = serializers.DateTimeField(required=False)  

class LCDataSerializer(serializers.Serializer):
    time = serializers.DateTimeField(required=False) 

class UpsellDataSerializer(serializers.Serializer):
    early_checkin = ECDataSerializer(required=False)  
    late_checkout = LCDataSerializer(required=False)  
    only_eclc = serializers.BooleanField(required=False)  

class BaseSearchEngineResultsPageSerializer(serializers.Serializer):
    checkin = serializers.CharField(required=True)
    checkout = serializers.CharField(required=True)
    currency = serializers.CharField(required=False)
    language = serializers.CharField(validators=[validate_language],required=True, max_length=5)
    residency = serializers.CharField(required=False)
    timeout = serializers.IntegerField(required=False)
    guests = serializers.ListField(
        child=GuestSerializer(),
        required=False,
        max_length=9)
    upsells = UpsellDataSerializer(required=False)

    def validate_checkin(self, value):
        try:
            checkin_date = datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise serializers.ValidationError("Checkin is incorrect format !")
        today = datetime.now()
        max_date = today + timedelta(days=730)
        if checkin_date > max_date:
            raise serializers.ValidationError("no later than 730 days from the day on which the request is made.")
        return value
    
    def validate_checkout(self, value):
        try:
            checkout_date = datetime.strptime(value, '%Y-%m-%d')  # YYYY-MM-DD formatida
        except ValueError:
            raise serializers.ValidationError("Check - out dates are not in the correct format. Please use YYYY-MM-DD format.")
        checkin_date = datetime.strptime(self.initial_data['checkin'], '%Y-%m-%d')
        if checkout_date > checkin_date + timedelta(days=30):
            raise serializers.ValidationError("The Check - out date should not exceed 30 days from the check-in date.")
        return value
    
    def validate_currency(self, value):
        allowed_currencies = ['USD', 'EUR', 'GBP'] 

        if value and value not in allowed_currencies:
            raise serializers.ValidationError(f"The currency must be one of the {allowed_currencies} list.")
        return value
    
    
    def validate_residency(self, value):
        if value:
            if not re.match(r'^[a-z]{2}$', value):
                raise serializers.ValidationError("The Residency Code must consist of 2 lowercase letters.")
        return value
    

    def validate_timeout(self, value):
        if value is not None:
            if value < 0 or value > 100:
                raise serializers.ValidationError("The Timeout value should range from 0 to 100.")
        return value

    def validate_guests(self, value):
        if value is not None and len(value) > 9:
            raise serializers.ValidationError("The maximum number of rooms should be 9")
        return value


class RegionSearchEngineResultsPageSerializer(BaseSearchEngineResultsPageSerializer):
    region_id = serializers.IntegerField(required=True)

class HotelSearchEngineResultsPageSerializer(BaseSearchEngineResultsPageSerializer):
    ids = serializers.ListField(
        child=serializers.CharField(),
        required=True,
        max_length=300 )
    
    def validate_ids(self, value):
        if len(value) > 300:
            raise serializers.ValidationError("The maximum number of hotel identifiers should be 300.")
        return value

class OrderBookingFormSerializer(serializers.Serializer):
    partner_order_id = serializers.CharField(
        required=True,
        min_length=1,
        max_length=256
    )
    book_hash = serializers.CharField(
        required=True,
        min_length=1,
        max_length=256
    )
    language = serializers.CharField(
        validators=[validate_language],
        required=True,
        min_length=2,
        max_length=2
    )
    user_ip = serializers.CharField(
        required=True
    )

    def validate_partner_order_id(self, value):
        if not value:
            raise serializers.ValidationError("Partner order ID is required.")
        return value

    def validate_book_hash(self, value):
        if not value:
            raise serializers.ValidationError("Book hash is required.")
        return value



    def validate_user_ip(self, value):
        if not value:
            raise serializers.ValidationError("User IP is required.")
        return value

class CreditCardDataCoreSerializer(serializers.Serializer):
    year = serializers.CharField(
        required=True,
        min_length=2,
        max_length=2
    )
    card_number = serializers.CharField(
        required=True,
        min_length=13,
        max_length=19
    )
    card_holder = serializers.CharField(
        required=True,
        min_length=1
    )
    month = serializers.CharField(
        required=True,
        min_length=2,
        max_length=2
    )

class CreditCardDataTokenizationSerializer(serializers.Serializer):
    object_id = serializers.CharField(
        required=True,
        min_length=1,
        max_length=20
    )
    pay_uuid = serializers.CharField(
        required=True,
        min_length=36,
        max_length=36
    )
    init_uuid = serializers.CharField(
        required=True,
        min_length=36,
        max_length=36
    )
    user_first_name = serializers.CharField(
        required=True,
        min_length=1
    )
    user_last_name = serializers.CharField(
        required=True,
        min_length=1
    )
    cvc = serializers.CharField(
        required=False,
        min_length=3,
        max_length=3
    )
    is_cvc_required = serializers.BooleanField(required=True)
    credit_card_data_core = CreditCardDataCoreSerializer(required=True)

    def validate_object_id(self, value):
        if not value:
            raise serializers.ValidationError("Object ID is required.")
        return value

    def validate_pay_uuid(self, value):
        if not value:
            raise serializers.ValidationError("Pay UUID is required.")
        return value

    def validate_init_uuid(self, value):
        if not value:
            raise serializers.ValidationError("Init UUID is required.")
        return value

    def validate_user_first_name(self, value):
        if not value:
            raise serializers.ValidationError("User first name is required.")
        return value

    def validate_user_last_name(self, value):
        if not value:
            raise serializers.ValidationError("User last name is required.")
        return value

    def validate_cvc(self, value):
        if value and (len(value) != 3):
            raise serializers.ValidationError("CVC code must be exactly 3 digits.")
        return value

class BookingPartnerSerializer(serializers.Serializer):
    partner = serializers.JSONField(required=True, help_text="Partner’s information.")    
    partner_order_id = serializers.CharField(
        required=True,
        min_length=1,
        max_length=256,
        help_text="The partner’s unique booking identifier."
    )
    
    comment = serializers.CharField(
        required=False,
        allow_blank=True,
        min_length=1,
        max_length=256,
        help_text="Partner’s booking’s internal comment. "
                  "These comments are not sent to the hotel and are not processed by the Emerging Travel Group Support Team. "
                  "They are visible only to the partner itself."
    )
    
    amount_sell_b2b2c = serializers.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        min_value=1,
        help_text="Resell price for the client in the contract currency. "
                  "The minimum value is 1."
    )
class BookingPaymentSerializer

class OrderBookingFinishSerializer(serializers.Serializer):
    arrival_datetime = serializers.DateTimeField(required=True)
    language = serializers.CharField(validators=[validate_language], required=True)
    partner = serializers.ListField(child=BookingPartnerSerializer(), required=True)