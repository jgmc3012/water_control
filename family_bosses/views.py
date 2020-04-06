from rest_framework import viewsets

from .serializers import FamilyBossSerializer

from .models import FamilyBoss

class FamilyBossViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FamilyBoss.objects.all()
    serializer_class = FamilyBossSerializer