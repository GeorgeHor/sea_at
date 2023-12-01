import time
import pytest
from selenium import webdriver
# from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.fixture(scope="function")
@pytest.fixture(scope="session")
def browser(request):
    browser = webdriver.Chrome()
    print("\n! ! ! start browser ! ! !")
    link = 'https://sea.softline.com.khoroshunovet.stage.slweb.cloud/licensing-center/agreements'
    # page_login = LoginPage(browser, link)
    # page_login.open()
    # page_login.authorization(login='lodevi5142@offsala.com', password='123456')
    browser.get(link)
    time.sleep(0)

    yield browser
    print("\n! ! ! quit browser ! ! !")
    browser.quit()
