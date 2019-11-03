from behave import when
from selenium.webdriver.common.by import By

ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CLOSING_X_SIDE_SECTION = (By.ID, )
ONE_TIME_BUTTON = (By.XPATH, "//div[@role='radio']//i[contains(@class, 'a-accordion-radio')]")

@when('Click Add to the card button')
def open_amazon(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when('Close suggestion side section')
def close_side_suggestion(context):
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()
#    else:
#       pass


@when('Select one-time purchase')
def select_radio_button(context):
    context.driver.find_element(*ONE_TIME_BUTTON).click()




