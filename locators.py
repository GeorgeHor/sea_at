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
    FULFILLMENT_BUTTON = By.CSS_SELECTOR, "a[href = '/licensing-center/fulfillment'].s - text - element"

class SetupInProgressPageLocators():
    SEA_PAGE_SETUP = By.CSS_SELECTOR, ".c-status-window__title"
