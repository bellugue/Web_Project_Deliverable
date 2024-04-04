from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Business, Car, AuthorisedDealer, Rent

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['NIF', 'name', 'location']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'AuthorisedDealer', 'licensePlate', 'model', 'mileage']
    list_filter = ['AuthorisedDealer']
    search_fields = ['name', 'licensePlate', 'model']

@admin.register(AuthorisedDealer)
class AuthorisedDealerAdmin(admin.ModelAdmin):
    list_display = ['id_authorisedDealer', 'NIF_bussines', 'location', 'schedule']

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['car_rented', 'id_authorisedDealer']
    list_filter = ['id_authorisedDealer']
    search_fields = ['car_rented__name']