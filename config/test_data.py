import os
import platform
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def get_executable_file_path_for(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '../resources/{}/{}'.format(platform.system(), __executable_file_name(filename)))


def __executable_file_name(binary_file):
    return '{}.exe'.format(binary_file) if platform.system() == 'Windows' else binary_file


class TestData:
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    REPORTS_DIR = os.path.join(ROOT_DIR, 'reports')
    SCREENSHOTS_DIR = os.path.join(ROOT_DIR, 'reports', 'screenshots')
    SCREENSHOTS_FROM_REPORTS_PATH = "../screenshots/{}"
    SCREENSHOTS_FROM_ROOT_DIR_PATH = "../reports/screenshots/{}"
    CHROME_EXECUTABLE = get_executable_file_path_for("chromedriver")
    FIREFOX_EXECUTABLE = get_executable_file_path_for("geckodriver")
    FIREFOX_BINARY_FILE = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    BASE_URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    FIRST_NAME = 'John'
    LAST_NAME = 'Travolta'
    ZIP_CODE = 'MD-2001'
