from django.db import models

from django.utils.timezone import datetime

class Measurer(models.Model):
    measure = models.PositiveIntegerField(default=0)
    last_visit = models.DateField()
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