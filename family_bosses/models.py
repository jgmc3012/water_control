from django.db import models

from houses.models import House

class FamilyBoss(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=True, unique=True)
    card_id = models.PositiveIntegerField(unique=True)
    house = models.OneToOneField(House, on_delete=models.SET_NULL, null=True)