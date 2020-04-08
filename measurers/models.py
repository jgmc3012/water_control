from django.db import models

from django.utils.timezone import datetime

from django.db.models.signals import pre_save


class Measurer(models.Model):
    measure = models.PositiveIntegerField(default=0)
    last_visit = models.DateField(default=datetime.today)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_all(house_id:str):
        house_id = house_id.upper()
        measurer = Measurer.objects.filter(
            house__house_id=house_id).select_related('house').select_related('house__familyboss')
        return measurer.first()

    def register_visit(self, measure:int):
        last_visit = self.last_visit
        self.last_visit = datetime.now().date()
        self.measure = measure
        self.save()
        return last_visit
    
    def calculate_consumption(self, currency_measure:int):
        """
        Calcula el consumo de agua registrado desde la ultima visita
        Recibe la metrica actual del medidor.
        """
        return currency_measure - self.measure

    @staticmethod
    def exists(pk:int):
        return Measurer.objects.filter(pk=pk).exists()

def set_last_visit(sender, instance, *args, **kwargs):
    instance.last_visit = datetime.now().date()

pre_save.connect(set_last_visit, sender=Measurer)