from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterAccountPage(BasePage):
    REGISTER_PAGE = "/index.php?route=account/register"
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

    DEFAULT_FIRST_NAME = "Ivan"
    DEFAULT_LAST_NAME = "Ivanov"
    DEFAULT_EMAIL = "ivanov@mail.ru"
    DEFAULT_PHONE_NUMBER = "+79992223344"
    DEFAULT_PASSWORD = "qwerty1"

    def input_first_name(self, first_name):
        self.browser.find_element(*RegisterAccountPage.FIRST_NAME_INPUT).click()
        self.browser.find_element(*RegisterAccountPage.FIRST_NAME_INPUT).clear()
        self.browser.find_element(*RegisterAccountPage.FIRST_NAME_INPUT).send_keys(first_name)

    def input_lastname(self, last_name):
        self.browser.find_element(*RegisterAccountPage.LASTNAME_INPUT).click()
        self.browser.find_element(*RegisterAccountPage.LASTNAME_INPUT).clear()
        self.browser.find_element(*RegisterAccountPage.LASTNAME_INPUT).send_keys(last_name)

    def input_email(self, email):
        self.browser.find_element(*RegisterAccountPage.EMAIL_INPUT).click()
        self.browser.find_element(*RegisterAccountPage.EMAIL_INPUT).clear()
        self.browser.find_element(*RegisterAccountPage.EMAIL_INPUT).send_keys(email)

    def input_phone(self, phone):
        self.browser.find_element(*RegisterAccountPage.TELEPHONE_INPUT).click()
        self.browser.find_element(*RegisterAccountPage.TELEPHONE_INPUT).clear()
        self.browser.find_element(*RegisterAccountPage.TELEPHONE_INPUT).send_keys(phone)

    def input_password(self, password):
        self.browser.find_element(*RegisterAccountPage.PASSWORD_INPUT).click()
        self.browser.find_element(*RegisterAccountPage.PASSWORD_INPUT).clear()
        self.browser.find_element(*RegisterAccountPage.PASSWORD_INPUT).send_keys(password)

    def input_confirm_password(self, password):
        self.browser.find_element(*RegisterAccountPage.CONFIRM_PASSWORD_INPUT).click()
        self.browser.find_element(*RegisterAccountPage.CONFIRM_PASSWORD_INPUT).clear()
        self.browser.find_element(*RegisterAccountPage.CONFIRM_PASSWORD_INPUT).send_keys(password)
