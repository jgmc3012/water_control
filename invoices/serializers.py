from rest_framework import serializers

from .models import Invoice

from houses.serializers import HouseSerializerLink

from consumption_histories.serializers import ConsumptionHistorySerializer

class InvoiceSerializer(serializers.ModelSerializer):
    place = HouseSerializerLink()
    detail = ConsumptionHistorySerializer()
    client = serializers.ReadOnlyField(source='client.card_id')
    class Meta:
        model = Invoice
        fields = ['amount', 'client', 'place', 'paid', 'payment_date', 'created_at', 'description', 'detail']