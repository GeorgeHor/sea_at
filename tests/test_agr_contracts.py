from pages.agreements_conract_page import AgrContractPage


# Тест открывает ссылку соглашения в новой вкладке и сверяет почту
def test_open_link_agreements(active_user):
    page_agr_contracts = AgrContractPage(active_user, AgrContractPage)
    page_agr_contracts.go_to_agreement_and_contracts()
    page_agr_contracts.check_FIO_agreements()


def test_data_contract(active_user):
    page_agr_contracts = AgrContractPage(active_user, AgrContractPage)
    page_agr_contracts.go_to_agreement_and_contracts()
    page_agr_contracts.check_data_contract()


def test_go_to_products_from_card_contract(active_user):
    page_agr_contracts = AgrContractPage(active_user, AgrContractPage)
    page_agr_contracts.go_to_agreement_and_contracts()
    page_agr_contracts.transfer_from_contract_card_to_products()


