from decimal import Decimal

from django.db import models

from django.db.models.signals import pre_save

from family_bosses.models import FamilyBoss
from houses.models import House
from consumption_histories.models import ConsumptionHistory

from django.utils import timezone

class Invoice(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    client = models.ForeignKey(FamilyBoss, on_delete=models.CASCADE)
    place = models.ForeignKey(House, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, default='', blank=True)
    detail = models.ForeignKey(ConsumptionHistory, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} : {}'.format(self.client, self.place, self.created_at)

    def pay(self):
        self.paid = True
        self.payment_date = timezone.now()
        self.save()

def set_amount(sender, instance, *args, **kwargs):
    if instance.amount is None:
        price_per_mts3 = 1250
        price_without_consumption = 100
        #¡TEMPORAL!# Estas variables hay que colocarlas en la interfaz

        if instance.detail.consumption > 0:
            instance.amount = Decimal(instance.detail.consumption * price_per_mts3)
        else:
            instance.amount = Decimal(price_without_consumption)

pre_save.connect(set_amount, sender=Invoice)