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
    VENDOR_FIELD = By.CSS_SELECTOR, "input.s-text-input__field" #поле Вендор
    BASEALT_VENDOR = By.XPATH, "//span[text()='BaseAlt']"
    H1_HEADER= By.CSS_SELECTOR, "h1.s-header_h1"
    FIELD_COMMENT = By.CSS_SELECTOR, ".s-textarea__field"
    ADD_FILE = By.CSS_SELECTOR, ".s-file-upload-area .s-button"
    SUCCESSFUL_SENDING_PURCHASE = By.XPATH, "//h3[text()='Ваша заявка принята в работу.']"


class AgreementsAndContractsLocators:
    AGR_CONTRACTS_BOKOVIK = By.XPATH, "//div[text()='Соглашение и договоры']"
    AGREEMENT_LINK_H3 = By.CSS_SELECTOR, ".agreement-list__item .agreement__title_clickable"
    MAIL_AGREEMENTS = By.XPATH, "//span[text()='bofeneg981@hdrlog.com']"
    NAME_CONTRACT = By.XPATH, "//tbody//div[text()='111']"
    CARD_CONTRACT_H2 = By.XPATH,  "//h2[text()='Договор 111']"
    CARD_CONTRACT_TYPE = By.XPATH, "//div[contains(@class, 's-text-element') and text()='111']"
    CARD_CONTRACT_DATE = By.XPATH, "//div[text()='не применимо']"
    CARD_CONTRACT_SUMM = By.XPATH, "//div[contains(@class, 's-text-element') and contains(., '124,00')]"
    CARD_CONTRACT_BUTTON = By.XPATH, "//button//div[contains (@class, 's-text-element') and text()='Открыть документ']"
    BUTTON_GO_TO_PRODUCTS = By.XPATH, "//button//div[text()='Перейти к продуктам']"
    PRODUCT_FROM_CONTRACT = By.XPATH, "//div[text()='Автотестовый продукт 2']"
    PRODUCT_NUMBER_CONTACT = By.XPATH, "//div[@class='filter-list__block filter-list__block_chips-list']//div[text()='111']"