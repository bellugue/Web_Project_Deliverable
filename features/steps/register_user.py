from behave import *
from selenium.webdriver.common.by import By

from django.contrib.auth.models import User

use_step_matcher("parse")

@when('I register a new user')
def step_impl(context):
    for row in context.table:
        context.browser.get(context.get_url('register'))
        assert context.browser.current_url == context.get_url('register')
        context.browser.find_element(By.ID, 'email').send_keys(row['email'])
        context.browser.find_element(By.ID, 'username').send_keys(row['username'])
        context.browser.find_element(By.ID, 'password').send_keys(row['password'])
        context.browser.find_element(By.ID, 'password2').send_keys(row['password2'])
        #context.browser.find_element(By.ID, 'register-button').click()
        #find button
        context.browser.find_element(By.XPATH, '//button[text()="Register"]').click()
    assert User.objects.count() == 1

@then(u'I\'m viewing the main page')
def step_impl(context):
    assert context.get_url('homePage') in context.browser.current_url  # Check if it is substring due to deep-linking