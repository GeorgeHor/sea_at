import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators
from selenium.webdriver.chrome.options import Options


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def wait_element(self, locator):
        pass
        # WebDriverWait(self, 10).until(EC.element_to_be_clickable(self))
        # WebDriverWait(self, 10).until(EC.presence_of_element_located(self))
