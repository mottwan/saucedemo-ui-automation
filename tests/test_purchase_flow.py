from common.header_bar import HeaderBar
from config.test_data import TestData
from pages.cart_page import CartPage
from pages.checkout_page import (CheckoutStepOnePage,
                                 CheckoutStepTwoPage,
                                 CheckoutCompletePage)
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from tests.base_test import BaseTest


class TestPurchaseFlow(BaseTest):

    def test_purchase_flow(self):
        login_page = LoginPage(self.driver)
        login_page.login(username=TestData.USERNAME, password=TestData.PASSWORD)

        inventory_page = ProductsPage(self.driver)
        assert inventory_page.page_should_be_loaded()

        products = inventory_page.get_products_list()
        items_to_shopping_cart = inventory_page.add_to_shopping_cart(products)

        header_bar = HeaderBar(self.driver)
        header_bar.click_on_shopping_cart()

        cart_page = CartPage(self.driver)
        items_from_shopping_cart = cart_page.get_cart_items()
        assert cart_page.check_items(items_to_shopping_cart, items_from_shopping_cart)
        cart_page.click_order_checkout()

        checkout_start_page = CheckoutStepOnePage(self.driver)
        assert checkout_start_page.should_be_loaded()
        checkout_start_page.enter_checkout_information(first_name=TestData.FIRST_NAME,
                                                       last_name=TestData.LAST_NAME, zip_code=TestData.ZIP_CODE)
        checkout_start_page.click_continue_checkout()

        checkout_overview_page = CheckoutStepTwoPage(self.driver)
        checkout_overview_page.should_be_loaded()

        assert checkout_overview_page.check_products(products)
        assert checkout_overview_page.count_item_total_amount(
            products) == checkout_overview_page.get_item_total_amount()
        assert checkout_overview_page.count_total_plus_tax_amount() == checkout_overview_page.get_total_amount()

        checkout_overview_page.click_finish_checkout()

        checkout_finish_page = CheckoutCompletePage(self.driver)
        assert checkout_finish_page.should_be_loaded()
        header_bar.click_on_shopping_cart()
        assert cart_page.should_be_equal_with() == 0
