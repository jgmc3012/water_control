from rest_framework import serializers

from .models import FamilyBoss

class FamilyBossSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyBoss
        fields = ['first_name', 'last_name', 'email', 'house', 'card_id', 'house']
