from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_ADMIN_PAGE = "/admin/index.php?route=account/login"
    INPUT_USERNAME = (By.ID, "input-username")
    INPUT_PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")

    def input_username(self, user):
        self.input(self.INPUT_USERNAME, user)

    def input_password(self, password):
        self.input(self.INPUT_PASSWORD, password)

    def login_admin_page(self, url):
        self.go_to_page(url + self.LOGIN_ADMIN_PAGE)
        self.input_username("user")
        self.input_password("bitnami")
        self.driver.find_element(*LoginPage.SUBMIT_BUTTON).click()
