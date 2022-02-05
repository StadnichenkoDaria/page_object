from selenium.webdriver.common.by import By
# from BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
import logging
import time


class AdminPage(BasePage):
    ADMIN_PAGE = "/admin"
    CATALOG_MENU = (By.ID, "menu-catalog")
    PRODUCTS_PANEL = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')
    ADD_NEW_PRODUCT_BUTTON = (By.XPATH, '//*[@id="content"]//*[@class="fa fa-plus"]')
    PRODUCT_NAME_INPUT = (By.ID, "input-name1")
    META_TAG_TITLE_INPUT = (By.ID, "input-meta-title1",)
    DATA_TAB = (By.XPATH, '//*[@id="form-product"]//*[text()="Data"]')
    MODEL_INPUT = (By.ID, 'input-model',)
    SAVE_PRODUCT_BUTTON = (By.XPATH, '//*[@id="content"]//*[@class="fa fa-save"]')
    SUCCESS_ALERT = (By.XPATH, '//*[@id="content"]//*[contains(text(), '
                               '"Success: You have modified products!")]')
    PRODUCT_CHECKBOX = (By.XPATH, '//*[@id="form-product"]/div/table/tbody/tr[3]/td[1]/input',)
    PRODUCT_TRASH = (By.XPATH, '//*[@id="content"]//*[@class="fa fa-trash-o"]')

    # def __config_logger(self):
    #     self.logger = logging.getLogger(type(self).__name__)
    #     self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
    #     self.logger.setLevel(level=self.browser.log_level)

    # перейти на страницу "Товары"
    def go_to_product_page(self):
        self.click_element(self.CATALOG_MENU)
        self.click_element(self.PRODUCTS_PANEL)

    # нажать на кнопку "добавить новый товар"
    def click_add_new_product_button(self):
        self.click_element(self.ADD_NEW_PRODUCT_BUTTON)

    # ввести имя товара
    def product_name_input(self, product):
        self.input(self.PRODUCT_NAME_INPUT, product)

    # ввести тег-тайтл
    def meta_tag_title(self, tag):
        self.input(self.META_TAG_TITLE_INPUT, tag)

    # ввести назваение модели товара
    def model_input(self, model):
        self.click_element(self.DATA_TAB)
        self.input(self.MODEL_INPUT, model)

    # нажать кнопку "Сохранить"
    def press_save_button(self):
        self.click_element(self.SAVE_PRODUCT_BUTTON)

    # проверить алерт
    def check_alert_msg(self):
        self.check_element_presence(self.SUCCESS_ALERT)

    # добавить новый товар
    def add_new_product(self, name, tag_title, model):
        self.click_add_new_product_button()
        self.product_name_input(name)
        self.meta_tag_title(tag_title)
        self.model_input(model)
        self.press_save_button()

    # удалить товар
    def delete_product(self):
        self.click_element(self.PRODUCT_CHECKBOX)
        self.click_element(self.PRODUCT_TRASH)


