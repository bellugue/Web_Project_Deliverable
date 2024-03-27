from django.shortcuts import render
from django.views.generic import ListView

from Car_Renting.models import Car, AuthorisedDealer


# Create your views here.

def homePage(request):
    authorisedDealers = AuthorisedDealer.objects.all()
    return render(request, 'homePage.html', {'authorisedDealers': authorisedDealers})