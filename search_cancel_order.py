from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.XPATH, "//input[@type='search' and @name='help_keywords']")
SEARCH_SUBMIT = (By.XPATH, "//input[@class='a-button-input' and @type='submit']")
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='help-content']/h1")

@given('Open Amazon page1')
def open_google(context):
    context.driver.get('https://www.amazon.com')

@given('Open Help page1')
def open_google(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Input {search_word} into search field1')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)

@when('Click on search icon1')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)

@then('Product results for {search_word} are shown1')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word,
                                                                                                results_msg)
