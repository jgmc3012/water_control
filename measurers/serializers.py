from rest_framework import serializers

from .models import Measurer

class MeasurerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurer
        fields = ['measure']
