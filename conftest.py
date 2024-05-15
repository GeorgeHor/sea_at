import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    print("\n! ! ! start browser ! ! !")
    browser.maximize_window()
    yield browser

    print("\n! ! ! quit browser ! ! !")
    browser.quit()


# авторизация под неактивным юзером id=53
@pytest.fixture(scope="function")
def not_active_user(browser):
    link = 'https://sea.softline.com.khoroshunovet.stage.slweb.cloud/licensing-center'
    page_login = LoginPage(browser, link)
    page_login.open()
    time.sleep(3)
    page_login.authorization(login='sigabe7254@weirby.com', password='sigabe7254@weirby.com')
    yield browser


# авторизация под активным юзером id = 44
@pytest.fixture(scope="function")
def active_user(browser):
    link = 'https://sea.softline.com.khoroshunovet.stage.slweb.cloud/licensing-center'
    page_login = LoginPage(browser, link)
    page_login.open()
    time.sleep(3)
    page_login.authorization(login='jitab97068@fryshare.com', password='jitab97068@fryshare.com')
    yield browser


