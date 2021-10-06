import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def set_driver_options(driver_opts):
    arguments = ['--no-sandbox', 'disable-infobars', '--disable-extensions', '--disable-gpu', '--disable-web-security']
    options = driver_opts
    for arg in arguments:
        options.add_argument(arg)
    return options
