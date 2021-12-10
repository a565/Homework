from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AuthPage(BasePage):
    _url = ('https://esia-portal1.test.gosuslugi.ru/')


    _sel = 'loginByPwdButton'
    login = 'login'
    pwd = 'password'

    def fill_login_input(self,login):
        AuthPage.get_element(self,By.ID,'login',_time_out = 5,driver=self._driver).send_keys(login)

    def fill_pwd_input(self,pwd):
        AuthPage.get_element(self,By.ID,'password',_time_out = 5,driver=self._driver).send_keys(pwd)

    def  check(self):
        AuthPage.get_element(self,By.ID,'ufoPC',_time_out = 5,driver=self._driver).click()

    def login_page(self):
        AuthPage.get_element(self,By.ID,'loginByPwdButton',_time_out = 5,driver=self._driver).click()



