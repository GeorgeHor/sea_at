import time

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ProductsPageLocators
from locators import DashboardPageLocators


class ProductsPage(BasePage):
    def highlight_element(self, element):
        try:
            # Добавляем красную рамку к элементу через JavaScript
            self.browser.execute_script("arguments[0].style.border='5px solid red'", element)
        except Exception as e:
            self.logger.error(f"Ошибка при добавлении стилей: {e}")

    def should_be_bybutton(self):
        self.logger.info("Ожидание кликабельности кнопки 'Купить' на странице Продукты")

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductsPageLocators.BY_BUTTON)
        )
        assert EC.element_to_be_clickable(ProductsPageLocators.BY_BUTTON)

    def click_to_all_products(self):
        self.logger.info("Ожидание кликабельности кнопки 'Все продукты'")
        WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable(DashboardPageLocators.PRODUCTS_BUTTON)
        )
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

    def check_validation_an_empty_products_form(self):
        self.logger.info('Проверка текста заголовка')
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(ProductsPageLocators.PURCHASE_REQUEST_BUTTON, 'Заявка на закупку'),
            "Заголовок формы не имеет тектс 'Заявка на закупку'"
        )
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductsPageLocators.SEND_BUTTON)
        )
        self.logger.info("Клик по кнопке Отправить")
        self.browser.find_element(*ProductsPageLocators.SEND_BUTTON).click()

        self.logger.info("Получаем текст")
        #Ожидание сообщения о валидации
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductsPageLocators.MESSAGE_VALIDATION)
        )
        assert EC.presence_of_element_located(ProductsPageLocators.MESSAGE_VALIDATION), "Нет сообщения о валдиации 'Обязательное поле'"
