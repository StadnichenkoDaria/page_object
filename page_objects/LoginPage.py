from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    INPUT_USERNAME = (By.ID, "input-username")
    INPUT_PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
