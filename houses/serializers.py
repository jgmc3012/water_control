from rest_framework import serializers

from .models import House

from measurers.serializers import MeasurerSerializer

class HouseSerializerLink(serializers.RelatedField):
    queryset = House.objects.all()

    def to_representation(self, value):
        return value.house_id

    def to_internal_value(self, house_id):
        try:
                return House.objects.get(house_id=house_id)
        except House.DoesNotExist:
            raise serializers.ValidationError(
            'House does not exist.'
            )

class HouseSerializer(serializers.ModelSerializer):
    measurer = MeasurerSerializer(read_only=True)
    class Meta:
        model = House
        fields = ['line1', 'line2', 'zip_code', 'house_id', 'measurer']