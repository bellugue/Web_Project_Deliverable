from behave import *

use_step_matcher("parse")

@when('I edit the rent with user "{user}", car "{car}"')
def step_impl(context, name):
    from Car_Renting.models import Rent
    rent = Rent.objects.get(user=user, car_rented=car)
    context.browser.visit(context.get_url('editar_reserva'))
    if context.browser.url == context.get_url('myrestaurants:restaurant_edit', restaurant.pk) \
            and context.browser.find_by_id('input-form'):
        form = context.browser.find_by_id('input-form')
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()