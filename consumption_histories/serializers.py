from rest_framework import serializers

from .models import ConsumptionHistory

class ConsumptionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumptionHistory
        fields = ['from_date', 'to_date', 'consumption', 'measurer']
