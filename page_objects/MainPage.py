from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    SEARCH = (By.ID, "search")
    CART = (By.ID, "cart")
    MENU = (By.ID, "menu")
    CONTENT = (By.ID, "content")
