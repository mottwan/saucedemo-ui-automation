import pytest
from config.webdriver import Chrome, Firefox
from config.test_data import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = Chrome.set_driver()
        web_driver.get(TestData.BASE_URL)
    if request.param == "firefox":
        web_driver = Firefox.set_driver()
        web_driver.get(TestData.BASE_URL)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
