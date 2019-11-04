from behave import then, when
from selenium.webdriver.common.by import By
from time import sleep

PRIME_BOXES = (By.XPATH, "//div[contains(@class, 'a-section benefit-box')]")


@when('Open Amazon Prime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('{expected_item_count} boxes are present')
def verify_amount_of_boxes(context, expected_item_count):
    sleep(3)
    actual_item_count = len(context.driver.find_elements(*PRIME_BOXES))

    print(type(expected_item_count))
    print(type(actual_item_count))

    assert actual_item_count == int(expected_item_count), \
        f'Expected {expected_item_count} items but got {actual_item_count}'
