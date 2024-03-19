from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPageSSOLocators:
    AUTH_LOGIN_SSO = By.CSS_SELECTOR, "input[name='login[email]']"
    AUTH_PASSWORD_SSO = By.CSS_SELECTOR, "input[type=password]"
    AUTH_BUTTON_SSO = By.CSS_SELECTOR, "input[name=submit]"
    BUTTON_AUTH_SSO = By.CSS_SELECTOR, "button[type=submit]"


class DashboardPageLocators:
    COOKIEBOT_DIALOG_DENY_BUTTON = By.CSS_SELECTOR, "#CybotCookiebotDialogBodyButtonDecline"
    H1_HEADER = By.CSS_SELECTOR, ".ds-header_h1"
    ALL_DATE_BUTTON = By.CSS_SELECTOR, "a[href='/licensing-center/calendar'] .s-text-element"
    AGREEMENTS_BUTTON = By.CSS_SELECTOR, "a[href='/licensing-center/agreements'] .s-text-element"
    FULFILLMENT_BUTTON = By.CSS_SELECTOR, "a[href = '/licensing-center/fulfillment'] .s-text-element"
    PRODUCTS_BUTTON = By.CSS_SELECTOR, "a[href='/licensing-center/products'] .s-text-element"
    BENEFITS_BUTTON = By.CSS_SELECTOR, "a[href='/licensing-center/benefits'] .s-text-element"
    CONTACTS_BUTTON = By.CSS_SELECTOR, "a[href='/licensing-center/contacts'] .s-text-element"


class SetupInProgressPageLocators():
    SEA_PAGE_SETUP = By.CSS_SELECTOR, ".c-status-window__title"


class ProductsPageLocators:
    BY_BUTTON = By.CSS_SELECTOR, ".layout-with-sidebar-container__header button.s-button" #именно сама кнопка
    BY_BUTTON_TEXT = By.CSS_SELECTOR, ".layout-with-sidebar-container__header button.s-button .s-text-element"#для поиска текста
    PURCHASE_REQUEST_BUTTON = By.CSS_SELECTOR, ".s-header_h1"
    SEND_BUTTON = By.CSS_SELECTOR, ".layout-without-toolbar-control-block_right button.s-button_variant-filled .s-text-element" #Кнпока Отправить на форме
    MESSAGE_VALIDATION = By.XPATH, "(//*[text()='Обязательное поле'])[position()=1]"