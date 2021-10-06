from pages.base_page import BasePage
from config.locators import Locators


class ProductsPage(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def page_should_be_loaded(self):
        return self.check_page_loaded(*self.locator.APPLICATION_LOGO)

    def get_products_list(self):
        self.find_elements(*self.locator.INVENTORY_LIST)
        items = self.find_elements(*self.locator.INVENTORY_LIST)
        return [{'name': item.find_element(*self.locator.ITEM_NAME).text,
                 'price': item.find_element(*self.locator.ITEM_PRICE).text, 'quantity': 1} for item in items]

    def add_to_shopping_cart(self, items: list):
        products = self.find_elements(*self.locator.INVENTORY_LIST)
        for product in products:
            product_name = self.find_element(*self.locator.ITEM_NAME)
            for item in items:
                if item['name'] in product_name.text:
                    product.find_element(*self.locator.ADD_TO_CART).click()
        return items
