from django.db import models

from houses.models import House

class FamilyBoss(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=True, unique=True)
    card_id = models.PositiveIntegerField(unique=True)
    house = models.OneToOneField(House, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    def deactivate(self):
        if self.active:
            self.active = False
            self.house = None
            self.email = None
            self.save()

    def activate(self):
        if not self.active:
            self.active = True
            self.save()

    def has_pending_invoices(self):
        return self.invoice_set.filter(paid=False).exists()

    @staticmethod
    def inhabited_house(house_id):
        if house_id:
            house_id = house_id.upper()
            return FamilyBoss.objects.filter(house__house_id=house_id).exists()

    @staticmethod
    def disable(card_id):
        """
        Retorna un jefe de familia que tenga el card_id espeficicado y la propiedad active = False
        """
        return FamilyBoss.objects.filter(card_id=card_id, active=False).first()