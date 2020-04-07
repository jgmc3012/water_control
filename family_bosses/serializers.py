from rest_framework import serializers

from .models import FamilyBoss

from django.shortcuts import get_object_or_404
from houses.models import House

from houses.serializers import HouseSerializerLink


class FamilyBossSerializer(serializers.HyperlinkedModelSerializer):
    house = HouseSerializerLink()

    class Meta:
        model = FamilyBoss
        fields = ['first_name', 'last_name', 'email', 'card_id', 'house']
