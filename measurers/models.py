from django.db import models

from django.utils.timezone import datetime

class Measurer(models.Model):
    measure = models.PositiveIntegerField()
    last_visit = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} m3'.format(self.last_visit, self.measure)

    def register_visit(self, measure:int):
        last_visit = self.last_visit
        self.last_visit = datetime.today()
        self.measure = measure
        self.save()
        return last_visit