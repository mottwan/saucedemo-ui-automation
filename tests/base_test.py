import os
import sys
import unittest
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())

from utils.webdriver import WebBrowser


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = WebBrowser.set_name('chromedriver')
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
