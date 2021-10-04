import sys
sys.path.append(sys.path[0] + "/....")

from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import (CheckoutStepOnePage,
                                 CheckoutStepTwoPage,
                                 CheckoutCompletePage)
from common.header_bar import HeaderBar


class TestPurchaseFlow(BaseTest):

    def test_purchase_flow(self):
        login_page = LoginPage(self.driver)
        login_page.login(username='standard_user', password='secret_sauce')

        products_page = ProductsPage(self.driver)
        self.assertTrue(products_page.page_should_be_loaded())
        products = products_page.get_products_list()
        items_to_shopping_cart = products_page.add_to_shopping_cart(products)

        header_bar_component = HeaderBar(self.driver)
        header_bar_component.click_on_shopping_cart()

        cart_page = CartPage(self.driver)
        items_from_shopping_cart = cart_page.get_cart_items()
        self.assertTrue(cart_page.check_items(items_to_shopping_cart, items_from_shopping_cart))
        cart_page.click_order_checkout()

        checkout_step_one_page = CheckoutStepOnePage(self.driver)
        self.assertTrue(checkout_step_one_page.should_be_loaded())
        checkout_step_one_page.enter_checkout_information(first_name='John', last_name='Travolta', zip_code='MD-2001')
        checkout_step_one_page.click_continue_checkout()

        checkout_step_two_page = CheckoutStepTwoPage(self.driver)
        checkout_step_two_page.should_be_loaded()

        self.assertTrue(checkout_step_two_page.check_products(products),
                        'Verify that selected items are in shopping cart')
        self.assertEqual(checkout_step_two_page.count_item_total_amount(products),
                         checkout_step_two_page.get_item_total_amount(), 'Verify Total amount without tax')
        self.assertEqual(checkout_step_two_page.count_total_plus_tax_amount(),
                         checkout_step_two_page.get_total_amount(),
                         'Total amount plus tax is fine')

        checkout_step_two_page.click_finish_checkout()

        checkout_page_complete = CheckoutCompletePage(self.driver)
        self.assertTrue(checkout_page_complete.should_be_loaded())
        header_bar_component.click_on_shopping_cart()
        self.assertEqual(cart_page.should_be_empty(), 0, 'Verify that shopping cart is empty')
