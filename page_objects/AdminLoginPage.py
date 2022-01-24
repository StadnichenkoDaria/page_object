from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminLoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, '//*[@class ="btn btn-primary"]')
    # todo может быть эту страницу полностью удалить и оставить LoginPage, проверить совпадают ли локаторы
