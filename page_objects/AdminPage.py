import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


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

    @allure.step("Переход на страницу товаров")
    def go_to_product_page(self):
        self.click_element(self.CATALOG_MENU)
        self.click_element(self.PRODUCTS_PANEL)

    @allure.step("Клик на кнопку Добавить новый товар")
    def click_add_new_product_button(self):
        self.click_element(self.ADD_NEW_PRODUCT_BUTTON)

    @allure.step("Ввод названия товара")
    def product_name_input(self, product):
        self.input(self.PRODUCT_NAME_INPUT, product)

    @allure.step("Ввод тег-тайтла")
    def meta_tag_title(self, tag):
        self.input(self.META_TAG_TITLE_INPUT, tag)

    @allure.step("Ввод модели товара")
    def model_input(self, model):
        self.click_element(self.DATA_TAB)
        self.input(self.MODEL_INPUT, model)

    @allure.step("Нажатие на кнопку Сохранить")
    def press_save_button(self):
        self.click_element(self.SAVE_PRODUCT_BUTTON)

    @allure.step("Проверка наличия алерта")
    def check_alert_msg(self):
        self.check_element_presence(self.SUCCESS_ALERT)

    @allure.step("Добавление нового товара в раздел администрирования")
    def add_new_product(self, name, tag_title, model):
        self.click_add_new_product_button()
        self.product_name_input(name)
        self.meta_tag_title(tag_title)
        self.model_input(model)
        self.press_save_button()

    @allure.step("Удаление товара из раздела администрирования")
    def delete_product(self):
        self.click_element(self.PRODUCT_CHECKBOX)
        self.click_element(self.PRODUCT_TRASH)
