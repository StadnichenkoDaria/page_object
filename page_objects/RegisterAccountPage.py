from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterAccountPage(BasePage):
    CONTENT = (By.ID, "content")
    PERSONAL_DETAILS_AREA = (By.ID, "account")
    YOUR_PASSWORD_HEADER = (By.XPATH, "//*[text()='Your Password']")
    PASSWORD_INPUT = (By.ID, "input-password")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
