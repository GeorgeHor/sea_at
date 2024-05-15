from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging


class BasePage:

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

    def wait_for_element_presence(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=2):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
