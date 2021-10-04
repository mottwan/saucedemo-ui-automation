from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.locators import Locators


class SideMenu(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def click_on_logout(self):
        self.find_element(*self.locator.LOGOUT_LINK_TEXT).click()
        return LoginPage(self.driver)
