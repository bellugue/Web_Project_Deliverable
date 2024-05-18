# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Business, AuthorisedDealer, Car, Rent
from datetime import date, datetime, timedelta
from django.urls import reverse


# To execute the tests use command 'python manage.py test'

class BusinessModelTest(TestCase):

    def setUp(self):
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )

    def test_business_creation(self):
        self.assertEqual(self.business.NIF, '123456789')
        self.assertEqual(self.business.name, 'Test Business')
        self.assertEqual(self.business.location, 'Test Location')

    def test_business_deletion(self):
        self.business.delete()
        self.assertEqual(Business.objects.count(), 0)



class AuthorisedDealerModelTest(TestCase):

    def setUp(self):
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )
        self.authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='AD123',
            location='Dealer Location',
            schedule='9-5'
        )

    def test_authorised_dealer_creation(self):
        self.assertEqual(self.authorised_dealer.NIF_bussines, self.business)
        self.assertEqual(self.authorised_dealer.id_authorisedDealer, 'AD123')
        self.assertEqual(self.authorised_dealer.location, 'Dealer Location')
        self.assertEqual(self.authorised_dealer.schedule, '9-5')

    def test_authorised_dealer_deletion(self):
        self.authorised_dealer.delete()
        self.assertEqual(AuthorisedDealer.objects.count(), 0)



class CarModelTest(TestCase):

    def setUp(self):
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )
        self.authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='AD123',
            location='Dealer Location',
            schedule='9-5'
        )
        self.car = Car.objects.create(
            AuthorisedDealer=self.authorised_dealer,
            name='Test Car',
            licensePlate='ABC123',
            model='Model X',
            brand='Brand Y',
            mileage=1000
        )

    def test_car_creation(self):
        self.assertEqual(self.car.AuthorisedDealer, self.authorised_dealer)
        self.assertEqual(self.car.name, 'Test Car')
        self.assertEqual(self.car.licensePlate, 'ABC123')
        self.assertEqual(self.car.model, 'Model X')
        self.assertEqual(self.car.brand, 'Brand Y')
        self.assertEqual(self.car.mileage, 1000)

    def test_car_deletion(self):
        self.car.delete()
        self.assertEqual(Car.objects.count(), 0)



class RentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )
        self.authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='AD123',
            location='Dealer Location',
            schedule='9-5'
        )
        self.car = Car.objects.create(
            AuthorisedDealer=self.authorised_dealer,
            name='Test Car',
            licensePlate='ABC123',
            model='Model X',
            brand='Brand Y',
            mileage=1000
        )
        self.rent = Rent.objects.create(
            user=self.user,
            NIF=self.business,
            car_rented=self.car,
            id_authorisedDealer=self.authorised_dealer,
            fecha_entrada=date.today(),
            fecha_salida=date.today(),
            nombre_cliente='John Doe',
            telefono_cliente='1234567890',
            correo_cliente='john.doe@example.com'
        )

    def test_rent_creation(self):
        self.assertEqual(self.rent.user, self.user)
        self.assertEqual(self.rent.NIF, self.business)
        self.assertEqual(self.rent.car_rented, self.car)
        self.assertEqual(self.rent.id_authorisedDealer, self.authorised_dealer)
        self.assertEqual(self.rent.fecha_entrada, date.today())
        self.assertEqual(self.rent.fecha_salida, date.today())
        self.assertEqual(self.rent.nombre_cliente, 'John Doe')
        self.assertEqual(self.rent.telefono_cliente, '1234567890')
        self.assertEqual(self.rent.correo_cliente, 'john.doe@example.com')

    def test_rent_deletion(self):
        self.rent.delete()
        self.assertEqual(Rent.objects.count(), 0)


class CreateCarViewTest(TestCase):
    def setUp(self):
        # Crear un usuario para la prueba
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Crear una instancia de negocio y concesionario autorizado
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )
        self.authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='AD123',
            location='Dealer Location',
            schedule='9-5'
        )

        # Configurar el cliente para la prueba
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_create_car_view(self):
        # URL de la vista
        url = reverse('create_car')

        # Datos del formulario
        data = {
            'AuthorisedDealer': self.authorised_dealer.id,
            'name': 'Test Car',
            'licensePlate': 'ABC123',
            'model': 'Model X',
            'brand': 'Brand Y',
            'mileage': 1000
        }

        # Enviar una solicitud POST a la vista con los datos del formulario
        response = self.client.post(url, data)

        # Verificar que la solicitud redirige a la página de inicio (homePage)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('homePage'))

        # Verificar que el coche se ha creado en la base de datos
        self.assertEqual(Car.objects.count(), 1)
        car = Car.objects.first()
        self.assertEqual(car.name, 'Test Car')
        self.assertEqual(car.licensePlate, 'ABC123')
        self.assertEqual(car.model, 'Model X')
        self.assertEqual(car.brand, 'Brand Y')
        self.assertEqual(car.mileage, 1000)
        self.assertEqual(car.AuthorisedDealer, self.authorised_dealer)

class SeleccioCotxeViewTest(TestCase):

    def setUp(self):
        # Crear un usuario para la prueba
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Crear una instancia de negocio y concesionario autorizado
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )
        self.authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='AD123',
            location='Dealer Location',
            schedule='9-5'
        )

        # Crear una instancia de coche
        self.car = Car.objects.create(
            AuthorisedDealer=self.authorised_dealer,
            name='Test Car',
            licensePlate='ABC123',
            model='Model X',
            brand='Brand Y',
            mileage=1000
        )

        # Configurar el cliente para la prueba
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_seleccio_cotxe_view(self):
        # URL base de la vista
        base_url = reverse('seleccio_cotxe', args=[self.car.name, self.authorised_dealer.id_authorisedDealer])

        # Datos de GET (fecha de entrada y salida) en el formato esperado
        fecha_entrada = 'January 01, 2024'
        fecha_salida = 'January 10, 2024'
        url = f"{base_url}?fecha_entrada={fecha_entrada}&fecha_salida={fecha_salida}"

        # Datos del formulario POST
        post_data = {
            'fecha_entrada': '2024-01-01',
            'fecha_salida': '2024-01-10',
            'nombre_cliente': 'John Doe',
            'telefono_cliente': '1234567890',
            'correo_cliente': 'john.doe@example.com'
        }

        # Simular una solicitud POST a la vista con los datos del formulario
        response = self.client.post(url, post_data)

        # Verificar que la solicitud redirige a la vista de detalles del alquiler
        self.assertEqual(response.status_code, 302)
        rent = Rent.objects.first()
        self.assertRedirects(response, reverse('view_rent', args=[rent.pk]))

        # Verificar que el alquiler se ha creado en la base de datos con los datos correctos
        self.assertEqual(Rent.objects.count(), 1)
        rent = Rent.objects.first()
        self.assertEqual(rent.user, self.user)
        self.assertEqual(rent.NIF, self.business)
        self.assertEqual(rent.car_rented, self.car)
        self.assertEqual(rent.id_authorisedDealer, self.authorised_dealer)
        self.assertEqual(rent.fecha_entrada, datetime.strptime('2024-01-01', '%Y-%m-%d').date())
        self.assertEqual(rent.fecha_salida, datetime.strptime('2024-01-10', '%Y-%m-%d').date())
        self.assertEqual(rent.nombre_cliente, 'John Doe')
        self.assertEqual(rent.telefono_cliente, '1234567890')
        self.assertEqual(rent.correo_cliente, 'john.doe@example.com')



class ListCarsViewTest(TestCase):

    def setUp(self):
        # Crear un usuario para la prueba
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Crear una instancia de negocio y concesionario autorizado
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )
        self.authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='AD123',
            location='Dealer Location',
            schedule='9-5'
        )

        # Crear una instancia de coche
        self.car = Car.objects.create(
            AuthorisedDealer=self.authorised_dealer,
            name='Test Car',
            licensePlate='ABC123',
            model='Model X',
            brand='Brand Y',
            mileage=1000
        )

        # Configurar el cliente para la prueba
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_valid_date_form_submission(self):
        url = reverse('carList', args=[self.authorised_dealer.pk])
        fecha_entrada = date.today() + timedelta(days=1)
        fecha_salida = date.today() + timedelta(days=2)
        data = {
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('cars', response.context)
        self.assertEqual(response.context['fecha_entrada'], fecha_entrada)
        self.assertEqual(response.context['fecha_salida'], fecha_salida)

    def test_invalid_date_form_submission_past_fecha_entrada(self):
        url = reverse('carList', args=[self.authorised_dealer.pk])
        fecha_entrada = date.today() - timedelta(days=1)
        fecha_salida = date.today() + timedelta(days=2)
        data = {
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('error_message', response.context)
        self.assertEqual(response.context['error_message'], 'La fecha de entrada no puede ser anterior al día actual.')

    def test_invalid_date_form_submission_fecha_entrada_after_fecha_salida(self):
        url = reverse('carList', args=[self.authorised_dealer.pk])
        fecha_entrada = date.today() + timedelta(days=3)
        fecha_salida = date.today() + timedelta(days=2)
        data = {
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('error_message', response.context)
        self.assertEqual(response.context['error_message'], 'La fecha de entrada no puede ser superior a la fecha de salida.')

    def test_missing_date_form_submission(self):
        url = reverse('carList', args=[self.authorised_dealer.pk])
        data = {
            'fecha_entrada': '',
            'fecha_salida': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('error_message', response.context)
        self.assertEqual(response.context['error_message'], 'Debes seleccionar tanto la fecha de entrada como la fecha de salida.')


class EditRentFormTest(TestCase):
    def setUp(self):
        # Crear un usuario para la prueba
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Crear una instancia de negocio para la prueba
        self.business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )

        # Crear una instancia de concesionario autorizado para la prueba
        self.authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='test_authorised_dealer',
            location='Test Location',
            schedule='Test Schedule'
        )

        # Crear una instancia de coche para la prueba
        self.car = Car.objects.create(
            AuthorisedDealer=self.authorised_dealer,
            name='Test Car',
            licensePlate='Test License Plate',
            model='Test Model',
            brand='Test Brand',
            mileage=0
        )

        # Crear una instancia de renta para la prueba
        self.rent = Rent.objects.create(
            user=self.user,
            NIF=self.business,
            car_rented=self.car,
            id_authorisedDealer=self.authorised_dealer,  # Aquí se cambió de authorised_dealer a id_authorisedDealer
            fecha_entrada=datetime.now().date() + timedelta(days=1),
            fecha_salida=datetime.now().date() + timedelta(days=2),
            nombre_cliente='John Doe',
            telefono_cliente='1234567890',
            correo_cliente='john.doe@example.com'
        )

        # Configurar el cliente para la prueba
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_edit_rent_form_valid_submission(self):
        url = reverse('editar_reserva', args=[self.rent.pk])
        fecha_entrada = datetime.now().date() + timedelta(days=3)
        fecha_salida = datetime.now().date() + timedelta(days=4)
        data = {
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida,
            'nombre_cliente': 'Jane Doe',
            'telefono_cliente': '9876543210',
            'correo_cliente': 'jane.doe@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mis_reservas'))
        self.assertEqual(Rent.objects.count(), 1)
        updated_rent = Rent.objects.get(pk=self.rent.pk)
        self.assertEqual(updated_rent.nombre_cliente, 'Jane Doe')
        self.assertEqual(updated_rent.telefono_cliente, '9876543210')
        self.assertEqual(updated_rent.correo_cliente, 'jane.doe@example.com')

    def test_edit_rent_form_invalid_submission(self):
        url = reverse('editar_reserva', args=[self.rent.pk])
        fecha_entrada = datetime.now().date() - timedelta(days=1)  # Esto genera una fecha anterior a la actual
        fecha_salida = datetime.now().date() + timedelta(days=2)
        data = {
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida,
            'nombre_cliente': 'Jane Doe',
            'telefono_cliente': '9876543210',
            'correo_cliente': 'jane.doe@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_reserva.html')
        self.assertEqual(Rent.objects.count(), 1)
        updated_rent = Rent.objects.get(pk=self.rent.pk)
        self.assertNotEqual(updated_rent.fecha_entrada, fecha_entrada)  # Esto comprueba que la fecha no ha sido cambiada
        self.assertEqual(updated_rent.fecha_salida, datetime.now().date() + timedelta(days=2))


