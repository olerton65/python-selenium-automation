from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, '#nav-signin-tooltip span')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@given('Open Amazon Prime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')

    # "//div[contains(@class, 'a-section benefit-box ')]"


@given('Open Amazon Dress B07JZ9C1HW page')
def open_amazon_dress(context):
    context.driver.get('https://www.amazon.com/gp/product/B07JZ9C1HW/?th=1')


@given('Open Amazon Jeans B07BKD8JCQ page')
def open_amazon_jeans(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BKD8JCQ/')


@when('Click on the hamburger menu')
def click_ham_menu(context):
    context.driver.find_element(*HAM_MENU).click()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()


@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()


@then('Verify cart has {expected_item_count} item')
def verify_item_count(context, expected_item_count):
    sleep(5)
    actual_items = context.driver.find_element(*CARD_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected {expected_item_count}, but got {actual_items}'


@then('Refresh and verify cart has {expected_item_count} item')
def verify_item_count(context, expected_item_count):
    context.driver.refresh()
    actual_items = context.driver.find_element(*CARD_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected {expected_item_count}, but got {actual_items}'



@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    sleep(3)

    #   print(len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)))

    actual_item_count = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))

    #   print(type(expected_item_count))
    #   print(type(actual_item_count))

    assert actual_item_count == int(expected_item_count), \
        f'Expected {expected_item_count} items but got {actual_item_count}'


@then('Verify that hamburger menu is present')
def verify_ham_menu(context):
    #   print('FIND ELEMENTS =>>')
    #   print(context.driver.find_elements(*HAM_MENU))
    #   print(type(context.driver.find_elements(*HAM_MENU)))

    print('FIND ELEMENT =>>')
    print(context.driver.find_element(*HAM_MENU))
    print(type(context.driver.find_element(*HAM_MENU)))


# ======================TOOLTIP====================================================


@when('Click on Sign In btn from Sign In tooltip')
def click_signin_in_tooltip(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_TOOLTIP)).click()


@then('Verify SignIn tooltip is present and clickable')
def wait_signin_tooltip_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_TOOLTIP))


@when('Wait until SignIn tooltip disappears')
def wait_signin_tooltip_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_TOOLTIP))


@then('Verify SignIn tooltip is not clickable')
def wait_signin_tooltip_not_clickable(context):
    # Wait until NOT
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_TOOLTIP))
    # assert EC.element_to_be_clickable(SIGN_IN_TOOLTIP) == False (REQUIRES IF STATEMENT)


# ==================Today_Deals=====================================


DEALS_UNDER_25_LINK = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")


@when('Store original windows')
def store_current_windows(context):
    # To call the variable in different methods
    context.original_window = context.driver.current_window_handle
    # To call the variable in different methods
    context.old_windows = context.driver.window_handles
    print('\noriginal_window\n', context.original_window)
    print('\nold_windows\n', context.old_windows)


@when('Click to open Deals under {expected_price}')
def click_to_open_deals_under_25(context, expected_price):
    context.driver.find_element(*DEALS_UNDER_25_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    current_windows = context.driver.window_handles
    print('\ncurrent_windows\n', current_windows)

    #  new_window = current_windows[1]
    #  print('\nnew_window\n', new_window)

    new_windows = current_windows
    for old_window in context.old_windows:
        new_windows.remove(old_window)

    print('\nnew_windows\n', new_windows)
    sleep(3)

    #  Switch to recently open window
    context.driver.switch_to_window(new_windows[0])


@then('User can close new window and switch back to original')
def close_and_switch_back(context):
    sleep(3)
    context.driver.close()
    sleep(3)
    context.driver.switch_to_window(context.original_window)

