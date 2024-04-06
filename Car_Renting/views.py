from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib.auth import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Car_Renting.forms import RentForm, DateForm
from Car_Renting.models import Car, AuthorisedDealer, Rent
from django.contrib.auth import logout,authenticate, login



# Create your views here.

def homePage(request):
    authorisedDealers = AuthorisedDealer.objects.all()
    return render(request, 'homePage.html', {'authorisedDealers': authorisedDealers})


def signIn(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('homePage')


def register(request):
    if request.method == 'GET':
        return render(request,'registration/register.html', {"from": UserCreationForm})

    else :
        if request.POST["password"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
                user.save()
                login(request, user)
                return redirect('homePage')
            except:
                return render(request, 'registration/register.html', {"form": UserCreationForm, "error": "Username already exists."})

    return render(request, 'registration/register.html', {"form": UserCreationForm, "error": "Passwords did not match."})

@login_required(login_url='login')
def list_cars(request, pk=None):
    context = {}
    if request.method == 'POST' and date_form.is_valid():
        fecha_entrada = form.cleaned_data['fecha_entrada']
        fecha_salida = form.cleaned_data['fecha_salida']

        if fecha_entrada and fecha_salida:
            print(fecha_entrada, fecha_salida)
            context = {
                'cars': cars,
                'fecha_entrada': fecha_entrada,
                'fecha_salida': fecha_salida,
            }
        else:
            context['error_message'] = 'Debes seleccionar tanto la fecha de entrada como la fecha de salida.'
    else:
        form = DateForm()

    context['date_form'] = form

    return render(request, 'carlist.html', context)

def reset_password(request):
    if request.method == 'POST':
        form = forms.PasswordResetForm(request.POST)
        if form.is_valid():
            user = form.save()
            signIn(request, user)
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
            if not car.is_reserved:
                # Modificar el formulario antes de guardarlo para establecer los valores predeterminados
                rent = form.save(commit=False)
                rent.NIF = dealer.NIF_bussines
                rent.car_rented = car
                rent.id_authorisedDealer = dealer
                rent.save()
                car.is_reserved = True
                car.save()
                return redirect('homePage')
            else:
                context['error_message'] = 'El cotxe seleccionat no esta disponible.'
                return redirect('seleccio_cotxe', car_name=car_name, dealer_id=dealer_id)

    else:
        # Completar automáticamente los campos del formulario con la información obtenida
        initial_data = {
            'NIF': dealer.NIF_bussines,
            'car_rented': car,
            'id_authorisedDealer': dealer
        }
        form = RentForm(initial=initial_data)
        # Establecer campos como solo lectura
        form.fields['NIF'].disabled = True
        form.fields['car_rented'].disabled = True
        form.fields['id_authorisedDealer'].disabled = True

    return render(request, 'car_selection.html', {'car': car, 'dealer': dealer, 'form': form})


def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('homePage')