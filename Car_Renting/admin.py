from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Business, Car, AuthorisedDealer, Rent

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['NIF', 'name', 'location']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'licensePlate', 'model', 'brand', 'mileage']

@admin.register(AuthorisedDealer)
class AuthorisedDealerAdmin(admin.ModelAdmin):
    list_display = ['id_authorisedDealer', 'location', 'schedule']

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['NIF', 'licensePlate', 'id_authorisedDealer', 'availability', 'price']
    list_filter = ['NIF', 'licensePlate', 'id_authorisedDealer']