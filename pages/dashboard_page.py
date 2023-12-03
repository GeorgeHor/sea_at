from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageSSOLocators
from selenium import webdriver
from locators import DashboardPageLocators


class DashboardPage(BasePage):
    # проверка есть ли плашки с ссылками на главной странице
    def should_be_dashboard_link(self):
        #добавили ожидание главной страницы 5 секунд
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(DashboardPageLocators.ALL_DATE_BUTTON)
        )
        assert self.is_element_present(*DashboardPageLocators.ALL_DATE_BUTTON), "Нет кнопки Все даты"
        assert self.is_element_present(DashboardPageLocators.AGREEMENTS_BUTTON)
        assert self.is_element_present(DashboardPageLocators.FULFILLMENT_BUTTON)
