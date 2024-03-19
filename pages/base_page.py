import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageSSOLocators
from selenium.webdriver.chrome.options import Options
import logging


class BasePage:

    # def __init__(self, browser, url):
    #     self.browser = browser
    #     self.url = url
    #     self.logger = logging.getLogger(__name__)
    #
    #     # Настройка обработчика для логирования
    #     self.logger.setLevel(logging.INFO)  # Установка уровня логирования
    #     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #
    #     # Настройка обработчика для вывода в консоль
    #     console_handler = logging.StreamHandler()
    #     console_handler.setFormatter(formatter)
    #     self.logger.addHandler(console_handler)

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(__name__)

        if not self.logger.handlers:  # Добавить обработчик только если его нет
            self.logger.setLevel(logging.INFO)  # Установка уровня логирования
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # Настройка обработчика для вывода в консоль
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

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

    # def is_element_clickable(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True
