from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30, default="")
    year = models.IntegerField(default=0)

    def __str__(self):
        return f"Car brand is {self.brand}, year manufactured is {self.year}"