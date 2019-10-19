from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.amazon.com')

sleep(1)

driver.find_element(By.XPATH, "//a[@id='nav-link-prime']/span[@class='nav-line-2 ']").click()

sleep(1)

driver.find_element(By.XPATH, "//div[@class='prime-button-try']/a").click()

sleep(1)

assert 'https://www.amazon.com/amazonprime' in driver.current_url

driver.quit()




