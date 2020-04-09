from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import InvoiceSerializer
from .models import Invoice

from rest_framework import status

from .utils import get_range_date

class InvoiceListView(APIView):
    serializer_class = InvoiceSerializer

    def get(self, request, year, month=None, day=None, *args, **kwargs):
        try:
            invoices = self.get_queryset(year,month,day)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(invoices, many=True)
        return Response(serializer.data)

    def get_queryset(self, year, month, day):
        from_date, to_date = get_range_date(year, month, day)
        invoices = Invoice.objects.filter(created_at__range=(from_date, to_date))
        return invoices

def visual_new_pay(request):
    return render(request, 'invoices/new_pay.html')