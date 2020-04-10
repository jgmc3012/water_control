from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

from .serializers import HouseSerializer

from .models import House
from measurers.models import Measurer

from django.contrib.auth.decorators import login_required
from rest_framework import permissions

class HouseViewListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def perform_create(self, serializer):
        serializer.save(measurer=Measurer.objects.create())

class HouseDetailView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@login_required()
def visual_create(request):
    return render(request, 'houses/create.html')