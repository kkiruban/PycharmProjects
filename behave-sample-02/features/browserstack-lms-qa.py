import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'acceptSslCerts': True,
 'javascript_enabled': True,
 'browser': 'Chrome',
 'browser_version': '80.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
    command_executor='https://kirubanandramasa2:a4cKHKQbrfqcQM9nyGAG@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver.get("https://training-lms-qa.redhat.com/sso/saml/auth/redhat")
print(driver.title)
time.sleep(20)
registerlink = driver.find_element_by_id("newMemberLink")
registerlink.click()
print(driver.title)
driver.quit()
