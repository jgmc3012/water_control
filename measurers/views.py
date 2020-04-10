from django.shortcuts import render

from .models import Measurer
from .serializers import MeasurerSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import create_consumption_and_invoice

from django.http import Http404

from django.contrib.auth.decorators import login_required
from rest_framework import permissions

class MeasurerUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def try_get_obj(self, house_id):
            measurer = Measurer.get_all(house_id)
            if not measurer:
                raise Http404('Measurer not found')
            return measurer

    def put(self, request, house_id, format='json'):
        data = request.data
        measurer = self.try_get_obj(house_id)
        measure = data.get('measure')

        serializer = MeasurerSerializer(measurer, data=data)
        if serializer.is_valid():
            measure = int(measure)
            if measure >= measurer.measure:
                res = create_consumption_and_invoice(measurer, measure)
                return Response(res)
            return Response({'Measure': 'La medida ingresada es inferior a la registrada en el sistema.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required()
def visual_update(request):
    return render(request, 'measurers/update.html')