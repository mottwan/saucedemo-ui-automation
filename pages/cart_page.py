import sys
# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.checkout_page import CheckoutStepOnePage
from utils.locators import *


class CartPage(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def get_cart_items(self):
        self.wait_element(*self.locator.CART_ITEM_LIST)
        cart_items = self.find_elements(*self.locator.CART_ITEM_LIST)
        return [{
            'name': item.find_element(*self.locator.ITEM_NAME).text,
            'price': item.find_element(*self.locator.ITEM_PRICE).text,
            'quantity': int(item.find_element(*self.locator.CART_ITEM_QTY).text)} for item in cart_items]

    def should_be_empty(self):
        try:
            self.find_element(*self.locator.CART_ITEM_LIST)
        except NoSuchElementException:
            return 0

    def click_order_checkout(self):
        self.find_element(*self.locator.CHECKOUT_BUTTON).click()
        return CheckoutStepOnePage(self.driver)

    @staticmethod
    def check_items(items1, items2):
        return True if items1 == items2 else False
