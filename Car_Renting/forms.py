from django import forms
from django.forms import DateInput

from .models import Rent, Car


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['fecha_entrada', 'fecha_salida', 'nombre_cliente', 'telefono_cliente', 'correo_cliente']
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }

class DateForm(forms.Form):
    fecha_entrada = forms.DateField(label='Fecha de entrada')
    fecha_salida = forms.DateField(label='Fecha de salida')
    widgets = {
        'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
        'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
    }

class CreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['AuthorisedDealer', 'name', 'licensePlate', 'model', 'brand', 'mileage']


class EditRentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['fecha_entrada', 'fecha_salida', 'nombre_cliente', 'telefono_cliente', 'correo_cliente']
        widgets = {
            'fecha_entrada': DateInput(attrs={'type': 'date'}),
            'fecha_salida': DateInput(attrs={'type': 'date'}),
        }
