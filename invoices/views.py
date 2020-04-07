from rest_framework import mixins
from rest_framework import generics

from .serializers import InvoiceSerializer

class InvoiceListView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    serializer_class = InvoiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self, data):
        breakpoint()
        print()