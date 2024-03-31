from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib.auth import forms
from Car_Renting.models import Car, AuthorisedDealer




# Create your views here.

def homePage(request):
    authorisedDealers = AuthorisedDealer.objects.all()
    return render(request, 'homePage.html', {'authorisedDealers': authorisedDealers})


def login(request):
    return render(request,'registration/login.html')
def register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the newly registered user
            return redirect('homePage')  # Redirect to your desired page after registration
    else:
        form = forms.UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)  # Ensure this line is present

def list_cars(request):
    cars = Car.objects.all()
    return render(request, 'carlist.html', {'cars' : cars})

def reset_password(request):
    if request.method == 'POST':
        form = forms.PasswordResetForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = forms.PasswordResetForm()
    context = {'form': form}
    return render(request, 'passwordReset.html', context)
