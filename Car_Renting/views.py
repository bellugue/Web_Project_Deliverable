from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib.auth import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from Car_Renting.forms import RentForm
from Car_Renting.models import Car, AuthorisedDealer, Rent



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

@login_required(login_url='login')
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


@login_required(login_url='login')
def seleccio_cotxe(request, car_name, dealer_id):
    car = get_object_or_404(Car, name=car_name)
    dealer = get_object_or_404(AuthorisedDealer, id_authorisedDealer=dealer_id)

    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            # Modificar el formulario antes de guardarlo para establecer los valores predeterminados
            rent = form.save(commit=False)
            rent.NIF = dealer.NIF_bussines
            rent.car_rented = car
            rent.id_authorisedDealer = dealer
            rent.save()
            return redirect('homePage')
    else:
        # Completar automáticamente los campos del formulario con la información obtenida
        initial_data = {
            'NIF': dealer.NIF_bussines,
            'car_rented': car,
            'id_authorisedDealer': dealer
        }
        form = RentForm(initial=initial_data)
        form.fields['NIF'].widget.attrs['readonly'] = True
        form.fields['car_rented'].widget.attrs['readonly'] = True
        form.fields['id_authorisedDealer'].widget.attrs['readonly'] = True

    return render(request, 'car_selection.html', {'car': car, 'dealer': dealer, 'form': form})



