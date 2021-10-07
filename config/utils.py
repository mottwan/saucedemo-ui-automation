import os
import sys
import glob
from datetime import datetime
from config.test_data import TestData

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def set_driver_options(driver_opts):
    arguments = ['--no-sandbox', 'disable-infobars', '--disable-extensions', '--disable-gpu', '--disable-web-security']
    options = driver_opts
    for arg in arguments:
        options.add_argument(arg)
    return options


def capture_screenshot(driver, name):
    # from pytest_html_reporter import attach
    # attach(data=driver.get_screenshot_as_png())
    driver.get_screenshot_as_file(os.path.join(TestData.ROOT_DIR, TestData.SCREENSHOTS_DIR, name))


def set_screenshot_name(report):
    test_file = report.fspath.split('/')[1].split('.py')[0] + '_'
    class_and_function_names = report.location[2].replace('.', '_') + '__'
    timestamp = datetime.now().strftime("%d_%m_%Y__%H-%M-%S__%f")
    return test_file + class_and_function_names + timestamp + ".png"


def inject_screenshot_into_html(screenshot_dir):
    return f'<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
           'onclick="window.open(this.src)" align="right"/></div>' % screenshot_dir


def append_extras(extra, *extra_types):
    return [extra.append(extra_type) for extra_type in extra_types]


def clean_up_screenshots_folder():
    screenshots = glob.glob(os.path.join(TestData.ROOT_DIR, "reports", "screenshots", "*"))
    for screenshot in screenshots:
        os.remove(screenshot)

