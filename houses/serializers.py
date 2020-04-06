from rest_framework import serializers

from .models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['line1', 'line2', 'zip_code', 'house_id']