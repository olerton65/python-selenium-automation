from behave import then, when
from selenium.webdriver.common.by import By


TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_RESULTS = (By.XPATH, "//li[@role='listitem']//a[.//span[@class='a-price']]")
PRODUCT_RESULT = (By.XPATH, "//a[contains(@href, 'Creed-Aventus-Parfum-Spray')]//span[@class='a-price-whole']")

@when('Open the first product search result')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULTS).click()


@when('Open the first product search result1')
def click_first_result1(context):
    context.driver.find_element(*PRODUCT_RESULT).click()


@then('Search results for {product} is shown')
def verify_result(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    assert product in result_text, f"Expected text is dress, but got {result_text}"
