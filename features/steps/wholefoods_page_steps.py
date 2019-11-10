from selenium.webdriver.common.by import By
from behave import given, then


PRODUCTS = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[5]//li")
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')


@given('Open Wholefoods Deals page')
def open_wholefoods_deal(context):
    context.driver.get(' https://www.amazon.com/wholefoodsdeals')


@then('Each product has a regular price and name')
def verify_regular_price(context):
    product_elements = context.driver.find_elements(*PRODUCTS)

    for product_element in product_elements:
        assert 'Regular' in product_element.text, f'Expected Regular to be in {product_element.text}'

        product_name = product_element.find_element(*PRODUCT_NAME).text
        # print('\n', product_name)
        assert '' != product_name, f'Expected non-empty product name'

