from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['amount', 'client', 'place', 'paid', 'payment_date', 'created_at', 'description']