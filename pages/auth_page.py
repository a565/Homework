from selenium.webdriver.common.by import By

from pages import base_page
from pages.base_page import BasePage

class AuthPage(BasePage):
    _url = ('https://esia-portal1.test.gosuslugi.ru/')



    _login_input =(By.ID, 'login')
    _pwd_input = (By.ID, 'password')
    _check = (By.ID, 'ufoPC')
    _login_button = (By.ID,'loginByPwdButton')
    _sel_typ = By.ID
    _sel = 'loginByPwdButton'
    login = 'login'
    pwd = 'password'


    def fill_login_input(self,login):
        self._driver.find_element(*self._login_input).send_keys(login)

    def fill_pwd_input(self,pwd):
        self._driver.find_element(*self._pwd_input).send_keys(pwd)

    def check(self):
        self._driver.find_element(*self._check).click()

    def login_page(self):
        self._driver.find_element(*self._login_button).click()

    def  check2(self):
        BasePage.get_element(By.ID,'ufoPC',_time_out = 5,driver=self._driver).click()

    def fill_login_input2(self,login):
        BasePage.get_element(By.ID,'login',_time_out = 5,driver=self._driver).send_keys(login)

    def fill_pwd_input2(self,pwd):
        BasePage.get_element(By.ID,'password',_time_out = 5,driver=self._driver).send_keys(pwd)

    def login_page2(self):
        BasePage.get_element(By.ID,'loginByPwdButton',_time_out = 5,driver=self._driver).click()



