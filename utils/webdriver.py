from selenium import webdriver
from .driverconf import get_executable_file_path_for


class WebBrowser:
    @staticmethod
    def set_name(browser_name: str):
        if browser_name.lower() in ['chrome', 'chromedriver', 'google-chrome', 'ch']:
            return Chrome.set_driver()
        elif browser_name.lower() in ['ff', 'firefox', 'gecko', 'geckodriver']:
            return Firefox.set_driver()


class Chrome:
    @staticmethod
    def set_driver():
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        return webdriver.Chrome(executable_path=get_executable_file_path_for('chromedriver'),
                                options=options)


class Firefox:
    @staticmethod
    def set_driver():
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        return webdriver.Firefox(executable_path=get_executable_file_path_for('geckodriver'),
                                 options=options)
