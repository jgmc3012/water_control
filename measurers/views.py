from .models import Measurer
from .serializers import MeasurerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from django.db import transaction

from consumption_histories.models import ConsumptionHistory


class MeasurerUpdate(APIView):
    def put(self, request, pk, format='json'):
        data = request.data
        measurer = get_object_or_404(Measurer, pk=pk)
        measure = data.get('measure')

        serializer = MeasurerSerializer(measurer, data=data)
        if serializer.is_valid():
            with transaction.atomic():
                consumption = measurer.calculate_consumption(measure)
                ConsumptionHistory.objects.create(
                    from_date = measurer.last_visit,
                    consumption = consumption,
                    measurer = measurer
                )
                measurer.register_visit(measure)
            data.update({
                'consumption' : consumption,
            })
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
