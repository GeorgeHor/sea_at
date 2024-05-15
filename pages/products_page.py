import time

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ProductsPageLocators
from locators import DashboardPageLocators
from selenium.common.exceptions import TimeoutException


class ProductsPage(BasePage):
    def highlight_element(self, element):
        try:
            # Добавляем красную рамку к элементу через JavaScript
            self.browser.execute_script("arguments[0].style.border='5px solid red'", element)
        except Exception as e:
            self.logger.error(f"Ошибка при добавлении стилей: {e}")

    def should_be_bybutton(self):
        self.logger.info("Ожидание кликабельности кнопки 'Купить' на странице Продукты")
        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(ProductsPageLocators.BY_BUTTON)
            )
        except TimeoutException:
            raise AssertionError ('Кнопка Купить не найдена')

    def click_to_all_products(self):
        self.logger.info("Ожидание кликабельности кнопки 'Продукты'")
        try:
            WebDriverWait(self.browser, 15).until(
                EC.element_to_be_clickable(DashboardPageLocators.PRODUCTS_BUTTON)
            )
        except TimeoutException:
            raise AssertionError("Кнопка Продукты не найдена")
        self.browser.find_element(*DashboardPageLocators.PRODUCTS_BUTTON).click()

    def click_to_bybutton(self):
        self.logger.info("Ожидание кликабельности кнопки 'Купить' на странице Продукты")
        #Ожидание кнопки Купить
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductsPageLocators.BY_BUTTON)
        )
        self.logger.info("Клик по кнопке Купить")
        # Находим элемент для функции
        element = self.browser.find_element(*ProductsPageLocators.BY_BUTTON)
        # Подсвечиваем нужную кнопку
        self.highlight_element(element)
        # Кликаем по нужной кнопке
        self.browser.find_element(*ProductsPageLocators.BY_BUTTON).click()


