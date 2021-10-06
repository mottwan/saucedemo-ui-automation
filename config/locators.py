from selenium.webdriver.common.by import By


class Locators(object):

    # Login Page Locators
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    # Header Bar Locators
    APPLICATION_LOGO = (By.CLASS_NAME, 'app_logo')
    CHECKOUT_HEADER_TITLE = (
        By.XPATH, '//*[@id="header_container"]//*[contains(text(), "Checkout: Your Information")]')
    SHOPPING_CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    INVENTORY_LIST = (By.CLASS_NAME, 'inventory_item')
    SIDE_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')

    # Cart Locators
    CART_ITEM_LIST = (By.CLASS_NAME, 'cart_item')
    CART_ITEM_QTY = (By.CLASS_NAME, 'cart_quantity')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    # Items Locators
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ADD_TO_CART = (By.XPATH, '//button[contains(text(), "Add to cart")]')
    REMOVE_FROM_CART = (By.XPATH, '//button[contains(text(), "Remove")]')

    # Checkout page step 1
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    # Checkout page step 2
    CHECKOUT_OVERVIEW = (By.XPATH, '//*[@id="header_container"]//*[contains(text(), "Checkout: Overview")]')
    FINISH_BUTTON = (By.ID, 'finish')
    ITEM_TOTAL_AMOUNT = (By.CLASS_NAME, 'summary_subtotal_label')
    TAX_AMOUNT = (By.CLASS_NAME, 'summary_tax_label')
    TOTAL_AMOUNT = (By.CLASS_NAME, 'summary_total_label')

    # Checkout page complete
    CHECKOUT_COMPLETE = (By.XPATH, '//*[@id="header_container"]//*[contains(text(), "Checkout: Complete!")]')

    # Side menu
    LOGOUT_LINK_TEXT = (By.ID, 'logout_sidebar_link')
