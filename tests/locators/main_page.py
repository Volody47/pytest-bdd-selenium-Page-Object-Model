from selenium.webdriver.common.by import By



class MainPageLocators():
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product a.link")
    STICKERS = (By.CSS_SELECTOR, ".sticker")
    CART_ITEMS_QUANTITY = (By.CSS_SELECTOR, "span.quantity")
    ADD_ITEM = (By.CSS_SELECTOR, ".product a.link")