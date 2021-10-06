from pages.base_page import BasePage
from config.locators import Locators


class CheckoutStepOnePage(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def should_be_loaded(self):
        return self.check_page_loaded(*self.locator.CHECKOUT_HEADER_TITLE)

    def enter_first_name(self, first_name):
        self.find_element(*self.locator.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_element(*self.locator.LAST_NAME).send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.find_element(*self.locator.ZIP_CODE).send_keys(zip_code)

    def enter_checkout_information(self, **checkout_info):
        self.enter_first_name(checkout_info['first_name'])
        self.enter_last_name(checkout_info['last_name'])
        self.enter_zip_code(checkout_info['zip_code'])

    def click_continue_checkout(self):
        self.find_element(*self.locator.CONTINUE_BUTTON).click()
        return CheckoutStepTwoPage(self.driver)


class CheckoutStepTwoPage(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def should_be_loaded(self):
        return self.check_page_loaded(*self.locator.CHECKOUT_OVERVIEW)

    def check_products(self, products):
        items = self.find_elements(*self.locator.CART_ITEM_LIST)
        for item in items:
            item_name = item.find_element(*self.locator.ITEM_NAME).text
            for product in products:
                if item_name == product['name']:
                    return True

    def click_finish_checkout(self):
        self.find_element(*self.locator.FINISH_BUTTON).click()
        return CheckoutCompletePage(self.driver)

    def get_item_total_amount(self):
        item_total = str(self.find_element(*self.locator.ITEM_TOTAL_AMOUNT).text).split('Item total: $')
        return float(item_total[1])

    def get_tax_amount(self):
        tax = str(self.find_element(*self.locator.TAX_AMOUNT).text).split('Tax: $')
        return float(tax[1])

    def get_total_amount(self):
        total = str(self.find_element(*self.locator.TOTAL_AMOUNT).text).split('Total: $')
        return float(total[1])

    def count_total_plus_tax_amount(self):
        return self.get_item_total_amount() + self.get_tax_amount()


    @staticmethod
    def count_item_total_amount(products):
        total_amount: float = 0.0
        for product in products:
            total_amount += float(product['price'][1:])
        return total_amount


class CheckoutCompletePage(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def should_be_loaded(self):
        return self.check_page_loaded(*self.locator.CHECKOUT_COMPLETE)
