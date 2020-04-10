"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.
before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.
before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.
before_tag(context, tag), after_tag(context, tag)
"""

# -- SETUP: Use cfparse as default matcher
# from behave import use_step_matcher
# step_matcher("cfparse")
import behave_webdriver
from selenium import webdriver
import logging
import time
import shutil
import os


# def before_all(context):
#     context.config.setup_logging()

# def before_feature(context, feature):
#     print("Before feature\n")
#     # Create logger
#     # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
#     context.logger = logging.getLogger('seleniumframework_tests')
#     hdlr = logging.FileHandler('./seleniumframework_tests.log')
#     formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#     hdlr.setFormatter(formatter)
#     context.logger.addHandler(hdlr)
#     context.logger.setLevel(logging.DEBUG)

from selenium import webdriver
from axe_selenium_python import Axe
from selenium.webdriver.chrome.options import Options


# def before_scenario(context, scenario):
#
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=1920x1080")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('blink-settings=imagesEnabled=false')
#     chrome_options.add_argument('--disable-gpu')
#
#     driver = webdriver.Chrome(options=chrome_options)
#     # if BROWSER == 'chrome':
#     #     context.browser = webdriver.Chrome()
#     # elif BROWSER == 'firefox':
#     #     context.browser = webdriver.Firefox()
#     # elif BROWSER == 'safari':
#     #     context.browser = webdriver.Safari()
#     # elif BROWSER == 'ie':
#     #     context.browser = webdriver.Ie()
#     # elif BROWSER == 'opera':
#     #     context.browser = webdriver.Opera()
#     # elif BROWSER == 'phantomjs':
#     #     context.browser = webdriver.PhantomJS()
#     # else:
#     #     print("Browser you entered:", BROWSER, "is invalid value")
#from selenium import webdriver # or any custom webdriver
from behave_webdriver.driver import BehaveDriverMixin
from behave_webdriver.steps import *
from seleniumrequests import RequestMixin # or your own mixin
#     driver.browser.maximize_window()
#     print("Before scenario\n")
import behave_webdriver


class BehaveRequestDriver(BehaveDriverMixin, RequestMixin, webdriver.Chrome):
    pass

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome.headless()
#
# def before_all(context):
#     context.behave_driver = behave_webdriver.Chrome()
# def before_all(context):
#     context.behave_driver = BehaveRequestDriver()

# def before_all(context):
#     context.behave_driver = behave_webdriver.Chrome.headless()

def after_all(context):
    # cleanup after tests run
    context.behave_driver.quit()
