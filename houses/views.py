from rest_framework import mixins
from rest_framework import generics

from .serializers import HouseSerializer

from .models import House
from measurers.models import Measurer


class HouseViewListCreate(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def perform_create(self, serializer):
        serializer.save(measurer=Measurer.objects.create())

class HouseDetailView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
