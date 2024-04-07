from django import forms
from .models import Rent


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['NIF', 'car_rented', 'id_authorisedDealer', 'fecha_entrada', 'fecha_salida', 'nombre_cliente', 'telefono_cliente', 'correo_cliente']
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
