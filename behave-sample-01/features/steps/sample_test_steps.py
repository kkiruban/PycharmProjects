from behave import then, given, when


@given(u'I am on the "Login" page')
def step_impl(context):
    context.browser.get('http://www.google.com')

@then(u'I should see "Log in to your Red Hat account"')
def step_impl(context):
    print(context.browser.title)
    #assert context.browser.title

@when(u'I navigate to qa user registration page')
def step_impl(context):
    print("step 3")

@when(u'I click on personal user radio button')
def step_impl(context):
    print("step 4")
