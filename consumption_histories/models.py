from django.db import models

from measurers.models import Measurer


class ConsumptionHistory(models.Model):
    from_date = models.DateField()
    to_date = models.DateField(auto_now_add=True)
    consumption = models.PositiveIntegerField()
    measurer = models.ForeignKey(Measurer, on_delete=models.CASCADE)
