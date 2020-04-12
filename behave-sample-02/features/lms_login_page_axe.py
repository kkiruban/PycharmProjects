from selenium import webdriver
from axe_selenium_python import Axe
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://training-lms-qa.redhat.com/sso/saml/auth/redhat")
print(driver.current_url)
print(driver.title)
axe = Axe(driver)
# Inject axe-core javascript into page.
axe.inject()
# Run axe accessibility checks.
results = axe.run()
# Write results to file
axe.write_results(results, 'a11y.json')
driver.close()
# Assert no violations are found
assert len(results["violations"]) == 0, axe.report(results["violations"])