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


def register(request):

    if request.method == 'POST':
        if request.method == 'POST':
            form = forms.UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = forms.UserCreationForm()

        context = {'form': form}
        return render(request, 'register.html', context)

    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the newly registered user
            return redirect('home')  # Redirect to your desired page after registration
    else:
        form = forms.UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)  # Ensure this line is present
