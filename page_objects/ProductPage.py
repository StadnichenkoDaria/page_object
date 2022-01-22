from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    PRODUCT_AREA = (By.ID, "product-product")
    THUMBNAILS = (By.CLASS_NAME, "thumbnails")
    BUTTON_CART = (By.ID, "button-cart")
    CONTENT = (By.ID, "content")
