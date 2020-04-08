from rest_framework import serializers

from .models import ConsumptionHistory

class ConsumptionHistorySerializer(serializers.ModelSerializer):
    measurer = serializers.ReadOnlyField(source='measurer.house.house_id')
    class Meta:
        model = ConsumptionHistory
        fields = ['from_date', 'to_date', 'consumption', 'measurer']
