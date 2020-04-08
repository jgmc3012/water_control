from .models import Measurer
from .serializers import MeasurerSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import create_consumption_and_invoice

from django.http import Http404

class MeasurerUpdate(APIView):

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
            res = create_consumption_and_invoice(measurer, measure)
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)