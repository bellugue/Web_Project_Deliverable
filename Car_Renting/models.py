from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Business(models.Model):
    NIF = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.NIF

class Car(models.Model):
    name = models.CharField(max_length=100)
    licensePlate = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    mileage = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AuthorisedDealer(models.Model):
    id_authorisedDealer = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return self.id_authorisedDealer

class Rent(models.Model):
    NIF = models.ForeignKey(Business, on_delete=models.CASCADE)
    licensePlate = models.ForeignKey(Car, on_delete=models.CASCADE)
    id_authorisedDealer = models.ForeignKey(AuthorisedDealer, on_delete=models.CASCADE)
    availability = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{str(self.id_authorisedDealer) + "@" + str(self.NIF) + "@" + str(self.licensePlate)}'