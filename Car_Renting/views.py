from datetime import date, datetime

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

    else:
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
    context = {'pk_authorised_dealer': pk}

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            fecha_entrada = form.cleaned_data['fecha_entrada']
            fecha_salida = form.cleaned_data['fecha_salida']

            # Validar que la fecha de entrada sea mayor o igual al día actual
            if fecha_entrada < date.today():
                context['error_message'] = 'La fecha de entrada no puede ser anterior al día actual.'
            elif fecha_entrada and fecha_salida:
                if fecha_entrada > fecha_salida:
                    context['error_message'] = 'La fecha de entrada no puede ser superior a la fecha de salida.'
                else:
                    # Aquí puedes procesar los datos del formulario o realizar cualquier acción necesaria
                    cars = get_available_cars(pk, fecha_entrada, fecha_salida)
                    context.update({
                        'cars': cars,  # Suponiendo que 'cars' está definido en otro lugar de tu vista
                        'fecha_entrada': fecha_entrada,
                        'fecha_salida': fecha_salida,
                    })
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
    fecha_entrada_str = request.GET.get('fecha_entrada')
    fecha_salida_str = request.GET.get('fecha_salida')

    # Convertir las cadenas de fecha a objetos datetime
    fecha_entrada = datetime.strptime(fecha_entrada_str, '%B %d, %Y').date()
    fecha_salida = datetime.strptime(fecha_salida_str, '%B %d, %Y').date()

    print(fecha_entrada, fecha_salida)
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
                rent.fecha_entrada = fecha_entrada
                rent.fecha_salida = fecha_salida
                rent.save()

                # Redireccionar a la homePage
                return redirect('view_rent', rent_id=rent.pk)
        else:
            error_message = 'El cotxe seleccionat no esta disponible.'
            return redirect('seleccio_cotxe', car_name=car_name, dealer_id=dealer_id)

    else:
        # Completar automáticamente los campos del formulario con la información obtenida
        initial_data = {
            'NIF': dealer.NIF_bussines,
            'car_rented': car,
            'id_authorisedDealer': dealer,
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida,
        }
        form = RentForm(initial=initial_data)
        # Make fields readonly
        form.fields['fecha_entrada'].widget.attrs['readonly'] = True
        form.fields['fecha_salida'].widget.attrs['readonly'] = True

    return render(request, 'car_selection.html', {'car': car, 'dealer': dealer, 'form': form})


def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('homePage')


def get_available_cars(authorised_dealer_pk, fecha_entrada, fecha_salida):
    """
    Retrieve available cars for the specified authorised dealer within the given date range.
    """
    authorised_dealer = get_object_or_404(AuthorisedDealer, pk=authorised_dealer_pk)

    # Get all cars associated with the authorised dealer
    all_cars = Car.objects.filter(AuthorisedDealer=authorised_dealer)


    # Get all rents that overlap with the specified date range
    overlapping_rents = Rent.objects.filter(
        id_authorisedDealer=authorised_dealer,
        fecha_entrada__lte=fecha_salida,
        fecha_salida__gte=fecha_entrada
    )

    # Extract car IDs from the overlapping rents
    reserved_car_ids = overlapping_rents.values_list('car_rented__id', flat=True)


    # Filter out reserved cars from the available cars
    available_cars = all_cars.exclude(id__in=reserved_car_ids)

    return available_cars

@login_required(login_url='login')
def view_rent(request, rent_id):
    # Obtener la reserva por su ID o mostrar un error 404 si no existe
    rent = get_object_or_404(Rent, pk=rent_id)
    return render(request, 'confirmRent.html', {'rent': rent})