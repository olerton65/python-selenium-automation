from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://www.amazon.com')

sleep(1)

driver.find_element(By.XPATH, "//a[@id='nav-hamburger-menu']/i").click()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/gp/help/customer/display.html?nodeId=508510&ref_=nav_em_T1_0_1_0_5_cs_help']")))
    element.click()

    element = driver.find_element(By.XPATH, "//input[@type='search' and @name='help_keywords']")
    element.clear()
    element.send_keys('cancel order')
    element = driver.find_element(By.XPATH, "//input[@class='a-button-input' and @type='submit']")
    element.click()

    assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

finally:
    driver.quit()




