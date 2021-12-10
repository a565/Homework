from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import operator
import time

class BasePage:
    _url = None
    _time_out = 5
    _sel_typ = By.ID
    text = ''

    def __init__(self,driver):
        self._driver=driver

    def open(self):
        self._driver.get(self._url)

    def get_element(self,_sel_typ, _sel, _time_out,driver):
       return WebDriverWait(driver, timeout=_time_out).until(
            expected_conditions.visibility_of_element_located((_sel_typ, _sel)))

    def get_elements(self,_sel_typ, _sel, _time_out, driver):
        return WebDriverWait(driver, timeout=_time_out).until(
            expected_conditions.visibility_of_any_elements_located((_sel_typ, _sel)))

    def text_is_displayed(self,text,_time_out,driver):
        time.sleep(_time_out)
        for element_ in driver.find_elements(By.XPATH, '//div'):
            if operator.contains(element_.text, text):
                return True
        return False



#contains_text()
'''
            for element_ in driver.find_elements(By.XPATH, '//div'):
                    print("Текст ищем : " )
                    if operator.contains(element_.text, text):
                            print("Текст найден: " + text)
                            return True
                            
                            
               try:
            element_ = driver.find_elements(By.XPATH, '//div')
            if operator.contains(element_.text, text):
                return True
        except NoSuchElementException: return False                    
'''