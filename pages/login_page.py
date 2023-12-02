from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageSSOLocators


class LoginPage(BasePage):
    # проверка нахождения инпута логина на странице
    def should_be_login_input(self):
        assert self.is_element_present(*LoginPageSSOLocators.AUTH_LOGIN_SSO), "Форма ввода логина не представлена на странице"

    # Ввод данных в инпуты и клик по кнопке для авторизации
    def authorization(self, login, password):
        self.browser.find_element(*LoginPageSSOLocators.AUTH_LOGIN_SSO).send_keys(login)

        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPageSSOLocators.AUTH_PASSWORD_SSO)).send_keys(password)

        self.browser.find_element(*LoginPageSSOLocators.AUTH_BUTTON_SSO).click()



        #второе окно авторизации, где нужно нажать на "авторизоваться"
        # WebDriverWait(self.browser, 5).until(
        #     EC.presence_of_element_located(LoginPageSSOLocators.BUTTON_AUTH_SSO))
        # self.browser.find_element(*LoginPageSSOLocators.BUTTON_AUTH_SSO).click()


