from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib.auth import forms
from Car_Renting.models import Car, AuthorisedDealer
from django.contrib.auth.forms import UserCreationForm




# Create your views here.

def homePage(request):
    authorisedDealers = AuthorisedDealer.objects.all()
    return render(request, 'homePage.html', {'authorisedDealers': authorisedDealers})


def login(request):
    return render(request,'registration/login.html')

def register(request):
    if request.method == 'GET':
        return render(request,'registration/register.html', {"from": UserCreationForm})

    else :
        if request.POST["password"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password"])
                user.save()
                login(request, user);
                return redirect('');
            except:
                return render(request, 'registration/register.html', {"form": UserCreationForm, "error": "Username already exists."})

    return render(request, 'registration/register.html', {"form": UserCreationForm, "error": "Passwords did not match."})

#<<<<<<< HEAD
#comment


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
#>>>>>>> master
