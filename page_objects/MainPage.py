from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    SEARCH = (By.ID, "search")
    CART = (By.ID, "cart")
    MENU = (By.ID, "menu")
    CONTENT = (By.ID, "content")
    CURRENCY_FORM = (By.ID, "form-currency",)
    POUND_CURRENCY = (By.XPATH, '//*[@id="form-currency"]//button[@name="GBP"]')
    EURO_CURRENCY = (By.XPATH, '//*[@id="form-currency"]//button[@name="EUR"]')
    US_CURRENCY = (By.XPATH, '//*[@id="form-currency"]//button[@name="USD"]')

    def switch_to_euro(self):
        self.click_element(self.CURRENCY_FORM)
        self.click_element(self.EURO_CURRENCY)

    def switch_to_pound(self):
        self.click_element(self.CURRENCY_FORM)
        self.click_element(self.POUND_CURRENCY)

    def switch_to_usd(self):
        self.click_element(self.CURRENCY_FORM)
        self.click_element(self.US_CURRENCY)
