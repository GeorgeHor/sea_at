import time

from pages.dashboard_page import DashboardPage
from pages.products_page import ProductsPage


def test_products(active_user):
    page_products = ProductsPage(active_user, ProductsPage)
    page_products.click_to_all_products()
    page_products.should_be_bybutton()
    page_products.click_to_bybutton()
    time.sleep(3)