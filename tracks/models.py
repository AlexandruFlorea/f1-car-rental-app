from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=128, null=False)
    location = models.CharField(max_length=128, null=False)
    length = models.IntegerField(default=0)
    average_g = models.IntegerField(default=0)

    def __str__(self):
        return f'Track object with ID: {self.id}'
