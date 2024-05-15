import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import SetupInProgressPageLocators
from pages.base_page import BasePage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class SetupInProgressPage(BasePage):
    # проверка надписи о настройке кабинета
    def setup_in_progress_page(self):
        #Ожидание нужного заголовка
        self.wait_for_element_presence(SetupInProgressPageLocators.SEA_PAGE_SETUP)
        # WebDriverWait(self.browser, 7).until(
        #     EC.presence_of_element_located(SetupInProgressPageLocators.SEA_PAGE_SETUP)
        # )

        # находим нужный заголовок и вытаскиваем из него текст
        test_123 = self.browser.find_element(*SetupInProgressPageLocators.SEA_PAGE_SETUP)
        text_element = test_123.text
        # сравниваем
        muma = "Мы настраиваем для вас Enterprise Agreement."
        assert text_element == muma, f"Текст в элементе '{text_element}' не соответствует ожидаемому тексту '{muma}'"
