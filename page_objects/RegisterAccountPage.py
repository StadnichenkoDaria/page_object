from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterAccountPage(BasePage):
    CONTENT = (By.ID, "content")
    PERSONAL_DETAILS_AREA = (By.ID, "account")
    YOUR_PASSWORD_HEADER = (By.XPATH, "//*[text()='Your Password']")
    PASSWORD_INPUT = (By.ID, "input-password")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    FIRST_NAME_INPUT = (By.ID, "input-firstname",)
    LASTNAME_INPUT = (By.ID, "input-lastname",)
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, '//*[@id="content"]//input[@type="checkbox"]',)
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]//input[@value="Continue"]')
    CREATE_USER_SUCCESS_TEXT = (By.XPATH, '//*[@id="content"]//*[contains(text(), "Your Account Has Been Created!")]')
