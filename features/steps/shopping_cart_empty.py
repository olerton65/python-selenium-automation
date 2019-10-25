from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_SUBMIT = (By.ID, 'nav-cart')
RESULTS_FOUND_MESSAGE = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")


@given('Open Amazon page2')
def open_google(context):
    context.driver.get('https://www.amazon.com')


@when('Click on search icon2')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown2')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)
