from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageSSOLocators
from selenium import webdriver
from locators import DashboardPageLocators
import logging


class DashboardPage(BasePage):
    # проверка есть ли плашки с ссылками на главной странице
    def should_be_dashboard_link(self):
        self.logger.info("Ожидание кнопки 'Все даты' на плашке")
        # #добавили ожидание главной страницы 12 секунд
        # WebDriverWait(self.browser, 12).until(
        #     EC.presence_of_element_located(DashboardPageLocators.ALL_DATE_BUTTON)
        # )
        self.wait_for_element_presence(DashboardPageLocators.ALL_DATE_BUTTON)
        self.logger.info("Проверка всех ссылок на плашках")
        assert self.wait_for_element_presence(DashboardPageLocators.ALL_DATE_BUTTON), "Нет кнопки Все даты"
        assert self.wait_for_element_presence(DashboardPageLocators.AGREEMENTS_BUTTON), "Нет плашки СОглашения"
        assert self.wait_for_element_presence(DashboardPageLocators.FULFILLMENT_BUTTON), "Нет плашки фулл"
        assert self.wait_for_element_presence(DashboardPageLocators.BENEFITS_BUTTON), "Нет плашки преимущества"
        assert self.wait_for_element_presence(DashboardPageLocators.PRODUCTS_BUTTON), "Нет плашки продукты"
        assert self.wait_for_element_presence(DashboardPageLocators.CONTACTS_BUTTON), "Нет плашки контакты"
