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
from Car_Renting.views import homePage, register, login, list_cars, reset_password, seleccio_cotxe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('login/',login, name='login'),
    path('register/',register,name='register'),
    path('carlist/<int:pk>/',list_cars, name='carList'),
    path('reset_password/', reset_password, name='reset_password'),
    path('coches/<str:car_name>/<str:dealer_id>/', seleccio_cotxe, name='seleccio_cotxe'),
]
