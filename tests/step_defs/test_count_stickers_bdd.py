
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from tests.page_model.main_page import MainPage
from tests.locators.main_page import MainPageLocators



# Scenarios
scenarios('../features/features.feature')


@given("I open url")
def load_url(browser):
    page = MainPage(browser)
    browser.get(page.url)

@then("I'm on the home page")
def right_page(browser):
    expected_url = MainPage(browser).url
    assert browser.current_url == expected_url

@when(parsers.parse('I looking for "{products}"'))
def looking_product(browser, products):
    page = MainPage(browser).search_products

@when(parsers.parse('I count the "{stickers}"'))
def search_stickers(browser, stickers):
    page = MainPage(browser).search_products
    i = 0
    for sticker in page:
        stickers = page[i].find_elements(*MainPageLocators.STICKERS)
        browser.stickers = stickers
        i += 1

@then("each product should have only one sticker")
def count_sticker(browser):
    assert len(browser.stickers) == 1, "Should be just one sticker for each item"



