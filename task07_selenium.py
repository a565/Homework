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

time.sleep(2)
'''
for elem in driver.find_elements(By.XPATH, '//input'):
    if elem.get_attribute('type') != 'hidden':
        if(elem.get_attribute('type')) == 'text':
            driver.find_element(By.XPATH, '//input').send_keys('a@test.ru')
            print(elem.get_attribute('type'))
        else:
            if (elem.get_attribute('type')) == 'password':
                driver.find_element_by_id('password').send_keys('12345')
                print(elem.get_attribute('type'))

time.sleep(2)


#driver.find_element_by_id('login').send_keys('12345')
driver.find_element_by_xpath('//input').send_keys('12345')
driver.find_element_by_id('password').send_keys('12345')
driver.find_element_by_xpath('//*[@id="loginByPwdButton"]').click()
'''
driver.quit()