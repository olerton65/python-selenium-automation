from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


TODAYS_DEALS_HEADER = (By.CSS_SELECTOR, "div.a-spacing-top-small h1.a-size-large[role='header']")
TODAYS_DEALS_PRODUCT = (By.XPATH, "//a[contains(@href,'Five-Minute-Journal')]")


@then('{expected_header} are shown')
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*TODAYS_DEALS_HEADER).text
    assert actual_header == expected_header, f'Expected {expected_header}, but got {actual_header}'


@then('Click on the {product} to add it to the cart')
def click_on_item(context, product):
    context.driver.wait.until(EC.element_to_be_clickable(TODAYS_DEALS_PRODUCT)).click()




