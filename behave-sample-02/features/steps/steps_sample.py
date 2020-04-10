from urllib.parse import urljoin

from behave import then, given, when

@given('I send a {method} request to the page "{page}"')
def send_request_page(context, method, page):
    url = urljoin(context.base_url, page)
    context.response = context.behave_driver.request(method, url)
