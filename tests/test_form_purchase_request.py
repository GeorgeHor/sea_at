import time
from pages.products_page import ProductsPage
from pages.purchase_products_page import PurchaseProductsPage


def test_purchase_form_validation(active_user):
    page_products = ProductsPage(active_user, ProductsPage)
    page_purchase_products = PurchaseProductsPage(active_user, PurchaseProductsPage)
    page_products.click_to_all_products()
    page_products.should_be_bybutton()
    page_products.click_to_bybutton()
    page_purchase_products.check_validation_an_empty_products_form()


def test_send_purchase_request(active_user):
    page_products = ProductsPage(active_user, ProductsPage)
    page_purchase_products = PurchaseProductsPage(active_user, PurchaseProductsPage)
    page_products.click_to_all_products()
    page_products.should_be_bybutton()
    page_products.click_to_bybutton()
    page_purchase_products.choose_vendor_basealt()
    page_purchase_products.write_comment()
    page_purchase_products.send_and_check()
