import os
from datetime import datetime

import pytest
from selenium import webdriver

from config.test_data import TestData
from config.utils import set_driver_options

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global driver
    if request.param is None or request.param == "chrome":
        from selenium.webdriver.chrome.options import Options
        driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE, options=set_driver_options(Options()))
        driver.get(TestData.BASE_URL)
    if request.param == "firefox":
        from selenium.webdriver.firefox.options import Options
        return webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE, options=set_driver_options(Options()))
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("tests/", "").replace("::", "_") + "-" + datetime.now().strftime(
                "%d-%m-%Y--%H-%M-%S--%f") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = f'<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % _screenshots_path(file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Swag Labs Python Test Automation!"


def _capture_screenshot(name):
    driver.get_screenshot_as_file(os.path.join(ROOT_DIR, "../reports/screenshots/{}".format(name)))


def _screenshots_path(screenshot):
    return "../screenshots/{}".format(screenshot)
