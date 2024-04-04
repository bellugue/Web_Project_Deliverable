from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib.auth import forms

from Car_Renting.forms import RentForm
from Car_Renting.models import Car, AuthorisedDealer



# Create your views here.

def homePage(request):
    authorisedDealers = AuthorisedDealer.objects.all()
    return render(request, 'homePage.html', {'authorisedDealers': authorisedDealers})


def login(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(request.POST)
    else:
        form = forms.AuthenticationForm()

    context = {'form': form}
    return render(request,'registration/login.html', context)
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

def list_cars(request, pk=None):
    if pk is not None:
        cars = Car.objects.filter(AuthorisedDealer=pk)
    else:
        cars = Car.objects.all()
    return render(request, 'carlist.html', {'cars': cars})

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

def seleccio_cotxe(request, car_name, dealer_id):
    car = get_object_or_404(Car, name=car_name)
    dealer = get_object_or_404(AuthorisedDealer, id_authorisedDealer=dealer_id)

    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a alguna página de éxito o haz lo que necesites después de guardar el formulario
            return redirect('homePage')
    else:
        # Completar automáticamente los campos del formulario con la información obtenida
        initial_data = {
            'NIF': dealer.NIF_bussines,
            'car_rented': car,
            'id_authorisedDealer': dealer
        }

        # Crear una instancia del formulario con los datos iniciales
        form = RentForm(initial=initial_data)

    return render(request, 'car_selection.html', {'car': car, 'dealer': dealer, 'form': form})