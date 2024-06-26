"""
URL configuration for First_Deliverable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Car_Renting.views import homePage, register, signIn, list_cars, reset_password, seleccio_cotxe, about_us, contact, \
    logout_view, view_rent, create_car, mis_reservas, editar_reserva, eliminar_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('login/', signIn, name='login'),
    path('register/',register,name='register'),
    path('carlist/<int:pk>/',list_cars, name='carList'),
    path('reset_password/', reset_password, name='reset_password'),
    path('coches/<str:car_name>/<str:dealer_id>/', seleccio_cotxe, name='seleccio_cotxe'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('logout/', logout_view, name='logout'),
    path('rent/<int:rent_id>/', view_rent, name='view_rent'),
    path('create_car/', create_car, name='create_car'),
    path('mis_reservas/', mis_reservas, name='mis_reservas'),
    path('editar_reserva/<int:rent_id>/', editar_reserva, name='editar_reserva'),
    path('eliminar_reserva/<int:reserva_id>/', eliminar_reserva, name='eliminar_reserva'),
]
