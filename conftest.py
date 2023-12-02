import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.fixture(scope="function")
@pytest.fixture(scope="session")
def browser(request):
    browser = webdriver.Chrome()
    print("\n! ! ! start browser ! ! !")

    yield browser

    print("\n! ! ! quit browser ! ! !")
    browser.quit()


# авторизация под неактивным юзером
@pytest.fixture(scope="session")
def not_active_user(browser):
    link = 'https://sea.softline.com.khoroshunovet.stage.slweb.cloud/licensing-center'
    page_login = LoginPage(browser, link)
    page_login.open()
    time.sleep(3)
    page_login.authorization(login='sigabe7254@weirby.com', password='sigabe7254@weirby.com')
    time.sleep(3)

    yield browser
