from django.shortcuts import render
from django.shortcuts import redirect
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
    queryset = FamilyBoss.objects.filter(active=True).select_related('house')
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

    @action(detail=True, methods=['put'])
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
        if instance.has_pending_invoices():
            return Response({'ok':False,'message':'Pending payments'})

        self.perform_destroy(instance)
        return Response({'ok':True}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.deactivate()

    def create(self, request, *args, **kwargs):
        if self.object_exists(request):
            return redirect('familyboss-detail', request.data.get('card_id'))
        if FamilyBoss.inhabited_house(request.data.get('house')):
            return Response({'house':'Ya existe un jefe de familia en ese lugar'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def object_exists(self, request, *args, **kwargs):
        card_id = request.data.get('card_id')
        if card_id:
            obj = FamilyBoss.disable(card_id)
            if obj:
                obj.activate()
                return True


def visual_create(request):
    return render(request, 'family_bosses/create.html')

def visual_edit(request):
    return render(request, 'family_bosses/edit.html')