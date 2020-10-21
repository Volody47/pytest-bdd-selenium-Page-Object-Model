from selenium.webdriver.common.by import By


class BasePageLocators():
    TITLE = (By.CSS_SELECTOR, "head>title")