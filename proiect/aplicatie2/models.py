from django.db import models
from aplicatie1.models import Location


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name