import time
from pages.auth_page import AuthPage
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

        time.sleep(2)
#        auth_page.fill_login_input('')
#        auth_page.fill_pwd_input('')

        auth_page.fill_login_input2('')
        auth_page.fill_pwd_input2('')

        auth_page.login_page2()

        time.sleep(2)


#        assert current_page.text_is_displayed(text='LOGIN EXCEPTION TEXT', timeout=10)

  #      driver.quit()