from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class BasePage:
    _url = None
    _time_out = 5
    _sel_typ = By.ID
    _sel ='login'

    def __init__(self,driver):
        self._driver=driver

    def open(self):
        self._driver.get(self._url)


    def get_element(_sel_typ, _sel, _time_out ,driver):
       login_btn = WebDriverWait(driver, timeout=_time_out).until(
            expected_conditions.visibility_of_element_located((_sel_typ, _sel)))
       return  login_btn


    def get_elements(_sel_typ, _sel, _time_out, driver):
        login_btn = WebDriverWait(driver, timeout=_time_out).until(
            expected_conditions.visibility_of_any_elements_located((_sel_typ, _sel)))
        return login_btn

 #   def text_is_displayed(text, timeout,driver):

#contains_text()

