from pages.base_page import BasePage
from pages.cart_page import CartPage
from common.side_menu import SideMenu
from utils.locators import Locators


class HeaderBar(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def click_on_shopping_cart(self):
        self.find_element(*self.locator.SHOPPING_CART_BUTTON).click()
        return CartPage(self.driver)

    def click_on_menu_button(self):
        self.find_element(*self.locator.SIDE_MENU_BUTTON).click()
        return SideMenu(self.driver)
