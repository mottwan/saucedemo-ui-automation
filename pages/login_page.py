import sys
# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from pages.base_page import BasePage
from utils.locators import Locators


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN_BUTTON).click()

    def login(self, **credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_login_button()
