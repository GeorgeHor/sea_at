import time

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ProductsPageLocators
from selenium.common.exceptions import TimeoutException


class PurchaseProductsPage(BasePage):

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
        # Ожидание сообщения о валидации
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductsPageLocators.MESSAGE_VALIDATION)
        )
        assert EC.presence_of_element_located \
            (ProductsPageLocators.MESSAGE_VALIDATION), "Нет сообщения о валдиации 'Обязательное поле'"

    def choose_vendor_basealt(self):
        self.logger.info('Ожидание кликабельности поля с вендорами')
        try:
            vendor_field_open = self.wait_for_element_clickable(ProductsPageLocators.VENDOR_FIELD)
            vendor_field_open.click()
        except TimeoutException:
            raise AssertionError('Поле с выбором вендора не найдено')
        time.sleep(7)

        # try:
        #     # vendor_field_open = self.wait_for_element_presence(ProductsPageLocators.VENDOR_FIELD)
        #
        #     basealt_vendor = self.wait_for_element_clickable(ProductsPageLocators.BASEALT_VENDOR)
        #     basealt_vendor.click()
        # except TimeoutException:
        #     raise AssertionError('Не смогли выбрать вендора BASEALT')
        # # self.browser.find_element(ProductsPageLocators.VENDOR_FIELD).click()
        # # self.browser.find_element(ProductsPageLocators.BASEALT_VENDOR).click()
        # self.logger.info("Клик по заголовку")
        # self.browser.find_element(ProductsPageLocators.H1_HEADER).click()
        #
        # self.logger.info("Перемещаем фокус на поле с комментарием")
        # self.browser.find_element(*ProductsPageLocators.FIELD_COMMENT).click()
        # WebDriverWait(self.browser, 10).until(
        #     EC.presence_of_element_located(ProductsPageLocators.VENDOR_FIELD)
        # )

    def write_comment(self):
        self.logger.info("Перемещаем фокус на поле с комментарием")
        field_comment = (self.browser.find_element(*ProductsPageLocators.FIELD_COMMENT))
        field_comment.click()
        field_comment.send_keys("Автотестовый коммент")

    def send_and_check(self):
        self.browser.find_element(*ProductsPageLocators.SEND_BUTTON).click()
        # Ождиаем заголовок об успешной отправке
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(ProductsPageLocators.SUCCESSFUL_SENDING_PURCHASE)
            )
            # Если за 10 сек заголовка нет, то кидаем исключение и выводим сообшение
        except TimeoutException:
            raise AssertionError("Заголовок 'Ваша заявка принята в работу.' не найден")

