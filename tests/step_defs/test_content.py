from pytest_bdd import scenarios, given, when, then, parsers


from tests.page_model.base_page import BasePage
from tests.page_model.main_page import MainPage

# Scenarios
scenarios('../acceptance/content.feature')


@given("I open url")
def load_url(browser):
    page = MainPage(browser)
    browser.get(page.url)

@then('There is a title shown on the page')
def step_impl(browser):
    page = BasePage(browser)
    assert page.title != None


@then(parsers.parse('The title tag has content "{content}"'))
def step_impl(browser, content):
    page = BasePage(browser)
    assert page.title.get_attribute("textContent") == content