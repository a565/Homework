from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class  ProfilePage(BasePage):
    _url =('https://esia-portal1.test.gosuslugi.ru/profile/user/personal')
    text = 'a1@mail.ru'

    def find_text(self, text, _time_out=5):
        return ProfilePage.text_is_displayed(self,text, _time_out, driver=self._driver)

    