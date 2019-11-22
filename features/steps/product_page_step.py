from behave import when, then
from selenium.webdriver.common.by import By

ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')
ONE_TIME_BUTTON = (By.XPATH, "//div[@role='radio']//i[contains(@class, 'a-accordion-radio')]")

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div#variation_color_name span.selection")

JEANS_COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li ")
SELECTED_JEANS_COLORS = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')


@when('Click Add to the cart btn')
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


@then('Verify user can select through colors')
def verify_colors(context):
    expected_colors = ['Black', 'Emerald', 'Ivory', 'Navy']

    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    #   print(color_webelements)

    # for x in range(len(color_webelements )):
    #   color_webelements[x].click()
    #   actual_color = context.driver.find_element(*SELECTED_COLOR).text

    #    print(actual_color)
    #    assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got {actual_color}'

    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        assert actual_color == expected_colors[color_webelements.index(color)]


@then('Verify user can select through all three colors')
def verify_jeans_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']

    color_elements = context.driver.find_elements(*JEANS_COLOR_OPTIONS)
    for x in range(len(color_elements)):
        color_elements[x].click()
        actual_color = context.driver.find_element(*SELECTED_JEANS_COLORS).text
        assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got{actual_color}'


@then('Click Add to the cart button')
def open_amazon(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
