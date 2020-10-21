from tests.locators.main_page import MainPageLocators
from tests.page_model.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @property
    def url(self):
        return super(MainPage, self).url + '/'

    @property
    def search_products(self):
        return self.browser.find_elements(*MainPageLocators.PRODUCT_ITEMS)


