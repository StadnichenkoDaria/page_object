from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def product_name_input(self, product):
        self.browser.find_element(*AdminPage.PRODUCT_NAME_INPUT).click()
        self.browser.find_element(*AdminPage.PRODUCT_NAME_INPUT).clear()
        self.browser.find_element(*AdminPage.PRODUCT_NAME_INPUT).send_keys(product)

    def meta_tag_title(self, tag):
        self.browser.find_element(*AdminPage.META_TAG_TITLE_INPUT).click()
        self.browser.find_element(*AdminPage.META_TAG_TITLE_INPUT).clear()
        self.browser.find_element(*AdminPage.META_TAG_TITLE_INPUT).send_keys(tag)

    def model_input(self, model):
        self.browser.find_element(*AdminPage.MODEL_INPUT).click()
        self.browser.find_element(*AdminPage.MODEL_INPUT).clear()
        self.browser.find_element(*AdminPage.MODEL_INPUT).send_keys(model)

    def go_to_product_panel(self):
        wait = WebDriverWait(self.browser, 3)
        self.browser.find_element(*AdminPage.CATALOG_MENU).click()
        wait.until(EC.visibility_of_element_located(AdminPage.PRODUCTS_PANEL))
        self.browser.find_element(*AdminPage.PRODUCTS_PANEL).click()
