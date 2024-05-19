from behave import *
from selenium.webdriver.common.by import By

from django.contrib.auth.models import User
from Car_Renting.models import Car  # Asegúrate de cambiar 'myapp' por el nombre real de tu aplicación

use_step_matcher("parse")


"""
@given('Exists restaurant registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from Car_Renting.models import 
    for row in context.table:
        restaurant = Restaurant(user=user)
        for heading in row.headings:
            setattr(restaurant, heading, row[heading])
        restaurant.save()
"""

@when('I log in as "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.get(context.get_url('login'))
    context.browser.find_element(By.ID, 'username').send_keys(username)
    context.browser.find_element(By.ID, 'password').send_keys(password)
    context.browser.find_element(By.XPATH, '//button[text()="Login"]').click()

@when('I add a new car')
def step_impl(context):
    setUp()
    for row in context.table:
        context.browser.get(context.get_url('create_car'))
        assert context.browser.current_url == context.get_url('create_car')
        context.browser.find_element(By.ID, 'id_AuthorisedDealer').send_keys(row['AuthorisedDealer'])
        context.browser.find_element(By.ID, 'id_name').send_keys(row['name'])
        context.browser.find_element(By.ID, 'id_licensePlate').send_keys(row['licensePlate'])
        context.browser.find_element(By.ID, 'id_model').send_keys(row['model'])
        context.browser.find_element(By.ID, 'id_brand').send_keys(row['brand'])
        context.browser.find_element(By.ID, 'id_mileage').send_keys(row['mileage'])
        context.browser.find_element(By.XPATH, '//button[text()="Afegir cotxe"]').click()
    assert Car.objects.count() == 1

@then('I\'m viewing the home page')
def step_impl(context):
    assert context.get_url('homePage') in context.browser.current_url


def setUp():
        business = Business.objects.create(
            NIF='123456789',
            name='Test Business',
            location='Test Location'
        )
        authorised_dealer = AuthorisedDealer.objects.create(
            NIF_bussines=self.business,
            id_authorisedDealer='Dealer1',
            location='Dealer Location',
            schedule='9-5'
        )