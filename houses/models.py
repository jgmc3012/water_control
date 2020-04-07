from django.db import models

from measurers.models import Measurer

from django.db.models.signals import pre_save

class House(models.Model):
    line1 = models.CharField(max_length=200, null=False, blank=False)
    line2 = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=20)
    house_id = models.CharField(max_length=20, unique=True)
    measurer = models.OneToOneField(Measurer, on_delete=models.CASCADE)

    def __str__(self):
        return self.house_id
    

def set_measurer(sender, instance, *args, **kwargs):
    if not instance.measurer:
        instance.measurer = Measurer.objects.create()

pre_save.connect(set_measurer, sender=House)