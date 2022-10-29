import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/Amit Manore/PycharmProjects/PythonTesting/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://unicreds.com/contact-us")
time.sleep(2)
driver.find_element(By.ID, 'fullname').send_keys('Amit Manore')
driver.find_element(By.NAME, 'email').send_keys('manore.amit@yahoo.com')

#Static Dropdown
#dropdown = Select(driver.find_element(By.CLASS_NAME, 'input-heading'))
#dropdown.select_by_visible_text('UK (+44)')
#dropdown.select_by_index(2)
driver.find_element(By.NAME, 'phone').send_keys('9619904256')
driver.find_element(By.ID, 'message').send_keys('Helloji Namaste!')

driver.find_element(By.ID, 'contactButton').click()

