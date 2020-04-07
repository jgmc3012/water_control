from django.db import models

from django.utils.timezone import datetime

from django.db.models.signals import pre_save


class Measurer(models.Model):
    measure = models.PositiveIntegerField(default=0)
    last_visit = models.DateField(default=datetime.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def register_visit(self, measure:int):
        last_visit = self.last_visit
        self.last_visit = datetime.today()
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
    instance.last_visit = datetime.today()

pre_save.connect(set_last_visit, sender=Measurer)