import time
from pages.auth_page import AuthPage
from pages.ProfilePage import ProfilePage
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function',name='driver')
def get_driver():
        return webdriver.Chrome(ChromeDriverManager().install())

class TestAuthPageTest:


    def test_auth_page(self,driver):
        auth_page = AuthPage(driver=driver)
        auth_page.open()


        auth_page.fill_login_input('')
        auth_page.fill_pwd_input('')

        auth_page.login_page()

        
        prof_page = ProfilePage(driver=driver)
        prof_page.open()

        assert prof_page.find_text('a1@mail.ru', _time_out=5)


        driver.quit()