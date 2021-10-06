from selenium import webdriver
from .test_data import TestData


class Chrome:
    @staticmethod
    def set_driver():
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        return webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE, options=options)


class Firefox:
    @staticmethod
    def set_driver():
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        return webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE, options=options)
