'''
На странице https://esia-portal1.test.gosuslugi.ru/ найти все элементы по xpath //input и заполнить логин/пароль.
Не заполнять те поля, которые имеют type="hidden".
'''
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://esia-portal1.test.gosuslugi.ru/')

time.sleep(2)

for elem in driver.find_elements(By.XPATH, '//input'):
    if elem.get_attribute('type') != 'hidden':
        elem.send_keys('text')

driver.quit()

