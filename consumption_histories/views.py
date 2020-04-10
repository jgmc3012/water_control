from .models import ConsumptionHistory
from .serializers import ConsumptionHistorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions

class ConsumptionHistoryListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """
    Listar los historiales de consumo o crear uno nuevo
    """
    def get(self, request, format=None):
        consumption_history = ConsumptionHistory.objects.all()
        serializer = ConsumptionHistorySerializer(consumption_history, many=True)
        return Response(serializer.data)