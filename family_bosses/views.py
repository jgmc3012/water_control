from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import FamilyBossSerializer
from invoices.serializers import InvoiceSerializer

from .models import FamilyBoss

from invoices.utils import pay_invoices

class FamilyBossViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FamilyBoss.objects.all().select_related('house')
    serializer_class = FamilyBossSerializer
    lookup_field = 'card_id'

    @action(detail=True, methods=['get'])
    def invoices(self, request, *args, **kwargs):
        family_boss = self.get_object()
        invoices = family_boss.invoice_set.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def pending_invoices(self, request, *args, **kwargs):
        family_boss = self.get_object()
        invoices = family_boss.invoice_set.filter(paid=False)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def pay_invoices(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        if amount:
            family_boss = self.get_object()
            invoices = family_boss.invoice_set.filter(paid=False).order_by('id')
            res = pay_invoices(invoices, amount)
            return Response(res)
        return Response({'message':'No se envio el amount'},status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.has_pending_invoices:
            return Response({'ok':False,'message':'Pending payments'})

        self.perform_destroy(instance)
        return Response({'ok':True}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.deactivate()