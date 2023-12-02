from selenium.webdriver.common.by import By


class LoginPageSSOLocators:
    AUTH_LOGIN_SSO = By.CSS_SELECTOR, "input[name='login[email]']"
    AUTH_PASSWORD_SSO = By.CSS_SELECTOR, "input[type=password]"
    AUTH_BUTTON_SSO = By.CSS_SELECTOR, "input[name=submit]"
    BUTTON_AUTH_SSO = By.CSS_SELECTOR, "button[type=submit]"


class DashboardPageLocators:
    COOKIEBOT_DIALOG_DENY_BUTTON = By.CSS_SELECTOR, "#CybotCookiebotDialogBodyButtonDecline"
    H1_HEADER = By.CSS_SELECTOR, ".ds-header_h1"
