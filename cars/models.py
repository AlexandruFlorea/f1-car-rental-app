from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    power_unit = models.CharField(max_length=128, unique=False, null=False)
    races_won = models.IntegerField(default=0)
    handling = models.CharField(max_length=128, null=False)
    price_per_lap = models.IntegerField(default=1000)


    def __str__(self):
        return f'Car object ID = {self.id}'

