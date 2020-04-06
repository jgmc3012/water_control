from django.db import models

from measurers.models import Measurer

class House(models.Model):
    line1 = models.CharField(max_length=200, null=False, blank=False)
    line2 = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    house_id = models.CharField(max_length=20, unique=True)
    measurer = models.OneToOneField(Measurer, on_delete=models.CASCADE)