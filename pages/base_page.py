from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.test_data import TestData


class BasePage(object):
    def __init__(self, driver, base_url=TestData.BASE_URL):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 10

    def check_page_loaded(self, *locator):
        self.wait_element(*locator)
        return bool(self.find_element(*locator))

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
