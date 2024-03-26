from django.shortcuts import render
from django.views.generic import ListView

from Car_Renting.models import Car


# Create your views here.

class CarRentingView(ListView):
    model = Car
    template_name =