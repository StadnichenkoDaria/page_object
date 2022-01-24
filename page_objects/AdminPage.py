from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
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
