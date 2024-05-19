from splinter.browser import Browser
from selenium import webdriver
from behave import fixture, use_fixture


def before_all(context):
    #context.browser = Browser('firefox', headless=True)
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    context.browser = webdriver.Firefox(options=options)


def after_all(context):
    context.browser.quit()
    context.browser = None


"""
@fixture
def browser_firefox(context):
    context.browser = webdriver.Firefox()
    yield context.browser
    context.browser.quit()

def before_all(context):
    use_fixture(browser_firefox, context)
"""
