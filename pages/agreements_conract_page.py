from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AgreementsAndContractsLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class AgrContractPage(BasePage):

    def go_to_agreement_and_contracts(self):
        # находит ссылку Соглашения и договоры в боковике и кликает по ней
        try:
            button_agr_and_contr = WebDriverWait(self.browser, 15).until(
                EC.element_to_be_clickable(AgreementsAndContractsLocators.AGR_CONTRACTS_BOKOVIK)
            )
            button_agr_and_contr.click()
        except TimeoutException:
            raise AssertionError('Раздел Соглашение и договоры в боковике не найден')
        # Проверяет наличие ссылки Соглашение на открытой странице
        try:
            # Объявляем переменную с ссылкой на соглашение
            self.agreement_link = self.wait_for_element_presence(AgreementsAndContractsLocators.AGREEMENT_LINK_H3)
        except TimeoutException:
            raise AssertionError('Ссылка на соглашение не найдена или страница не открылась')

    def check_FIO_agreements(self):
        # клик по ссылке Соглашнеие
        self.agreement_link.click()
        # Получаем идентификаторы всех открытых вкладок
        window_handles = self.browser.window_handles
        # Переключаемся на вторую вкладку
        self.browser.switch_to.window(window_handles[1])

        try:
            elem = self.wait_for_element_presence(AgreementsAndContractsLocators.MAIL_AGREEMENTS)
        except TimeoutException:
            raise AssertionError('Почта клиента, который принял соглашение не найдена')

        # Используется ActionChains для выполнения скролла к  элементу
        actions = ActionChains(self.browser)
        actions.move_to_element(elem).perform()

    def check_data_contract(self):
        try:
            number_contract = self.wait_for_element_presence(AgreementsAndContractsLocators.NAME_CONTRACT)
            number_contract.click()
        except TimeoutException:
            raise AssertionError('Номер договора "111" не найден')
        try:
            self.wait_for_element_presence(AgreementsAndContractsLocators.CARD_CONTRACT_TYPE)
            self.wait_for_element_presence(AgreementsAndContractsLocators.CARD_CONTRACT_DATE)
            self.wait_for_element_presence(AgreementsAndContractsLocators.CARD_CONTRACT_SUMM)
            self.wait_for_element_presence(AgreementsAndContractsLocators.CARD_CONTRACT_BUTTON)
        except TimeoutException:
            raise AssertionError('Каких-либо данных по договору не обнаружено')

    def transfer_from_contract_card_to_products(self):
        self.check_data_contract()
        try:
            button_go_to_product = self.wait_for_element_presence(AgreementsAndContractsLocators.BUTTON_GO_TO_PRODUCTS)
            button_go_to_product.click()
        except TimeoutException:
            raise AssertionError('Кнопка "Перейти к продуктам" не найдена на карточке договора')
        try:
            self.wait_for_element_presence(AgreementsAndContractsLocators.PRODUCT_FROM_CONTRACT)
            self.wait_for_element_presence(AgreementsAndContractsLocators.PRODUCT_NUMBER_CONTACT)
        except TimeoutException:
            raise AssertionError('Продукт не найден(или не найден номер договора в чипсах) или не сработал переход из карточки договора')
