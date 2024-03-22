from django.db import models


# Create your models here.
class CarListView(models.Model):
    def __str__(self):
        return self

class Car(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
