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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")


def pytest_html_report_title(report):
    report.title = "Swag Labs Python Test Automation!"
