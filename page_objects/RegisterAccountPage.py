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

    # ввести имя пользователя
    def input_first_name(self, first_name):
        self.input(self.FIRST_NAME_INPUT, first_name)

    # ввести фамилию пользователя
    def input_lastname(self, last_name):
        self.input(self.LASTNAME_INPUT, last_name)

    # ввести емейл пользователя
    def input_email(self, email):
        self.input(self.EMAIL_INPUT, email)

    # ввести номер телефона пользователя
    def input_phone(self, phone):
        self.input(self.TELEPHONE_INPUT, phone)

    # ввести пароль пользователя
    def input_password(self, password):
        self.input(self.PASSWORD_INPUT, password)

    # ввести подтверждение пароля
    def input_confirm_password(self, password):
        self.input(self.CONFIRM_PASSWORD_INPUT, password)

    # принять политику конфиденциальности
    def privacy_policy_accept(self):
        self.click_element(self.PRIVACY_POLICY_CHECKBOX)

    # нажать кнопку "Продолжить"
    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    # создать пользователя
    def create_user(self, name, lastname, email, phone, password, confirm_password):
        self.input_first_name(name)
        self.input_lastname(lastname)
        self.input_email(email)
        self.input_phone(phone)
        self.input_password(password)
        self.input_confirm_password(confirm_password)
