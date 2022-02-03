from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_ADMIN_PAGE = "/admin/index.php?route=account/login"
    INPUT_USERNAME = (By.ID, "input-username")
    INPUT_PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")

    def input_username(self, user):
        self.browser.find_element(*LoginPage.INPUT_USERNAME).click()
        self.browser.find_element(*LoginPage.INPUT_USERNAME).clear()
        self.browser.find_element(*LoginPage.INPUT_USERNAME).send_keys(user)

    def input_password(self, password):
        self.browser.find_element(*LoginPage.INPUT_PASSWORD).click()
        self.browser.find_element(*LoginPage.INPUT_PASSWORD).clear()
        self.browser.find_element(*LoginPage.INPUT_PASSWORD).send_keys(password)

    def login_admin_page(self):
        self.input_username("user")
        self.input_password("bitnami")
        self.browser.find_element(*LoginPage.SUBMIT_BUTTON).click()
