from lettuce.terrain import before
from selenium import webdriver

before

driver = webdriver.Firefox()

After

driver = webdriver.Remote(
  command_executor='https://key:secret@hub.testingbot.com/wd/hub',
  desired_capabilities=desired_caps)

def before_all(context):
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()