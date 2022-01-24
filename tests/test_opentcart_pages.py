import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.AdminPage import AdminPage
from page_objects.CategoryPage import CategoryPage
from page_objects.LoginPage import LoginPage
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegisterAccountPage import RegisterAccountPage


def test_visible_elements_main_page(browser):
    browser.get(browser.url)
    browser.find_element(*MainPage.SEARCH)
    browser.find_element(*MainPage.CART)
    browser.find_element(*MainPage.MENU)
    browser.find_element(*MainPage.CONTENT)


def test_visible_elements_product_macbook(browser):
    browser.get(browser.url + "/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("MacBook"))
    wait.until(EC.visibility_of_element_located(ProductPage.PRODUCT_AREA))
    wait.until(EC.visibility_of_element_located(ProductPage.THUMBNAILS))
    wait.until(EC.element_to_be_clickable(ProductPage.BUTTON_CART))
    wait.until(EC.text_to_be_present_in_element(ProductPage.BUTTON_CART, "Add to Cart"))


def test_visible_elements_login_page_external(browser):
    browser.get(browser.url + "/admin")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_USERNAME))
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_PASSWORD))
    wait.until(EC.visibility_of_element_located(LoginPage.SUBMIT_BUTTON))
    wait.until(EC.visibility_of_element_located(LoginPage.OPENCART_LINK))
    wait.until(EC.visibility_of_element_located(LoginPage.FORGOTTEN_PASSWORD))


def test_visible_elements_register_account(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.CONTENT))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.PERSONAL_DETAILS_AREA))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.YOUR_PASSWORD_HEADER))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.REGISTER_LINK))


def test_visible_elements_catalog(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(CategoryPage.CATEGORY_PAGE))
    wait.until(EC.visibility_of_element_located(CategoryPage.COLUMN_LEFT))
    wait.until(EC.element_to_be_clickable(CategoryPage.LIST_VIEW_BUTTON))
    wait.until(EC.element_to_be_clickable(CategoryPage.GRID_VIEW_BUTTON))
    wait.until(EC.text_to_be_present_in_element(CategoryPage.PRODUCT_COMPARE_LINK, "Product Compare"))


def test_add_new_product_admin_page(browser, login_admin_page):
    wait = WebDriverWait(browser, 3)
    browser.find_element(*AdminPage.CATALOG_MENU).click()
    wait.until(EC.visibility_of_element_located(AdminPage.PRODUCTS_PANEL))
    browser.find_element(*AdminPage.PRODUCTS_PANEL).click()
    browser.find_element(*AdminPage.ADD_NEW_PRODUCT_BUTTON).click()
    browser.find_element(*AdminPage.PRODUCT_NAME_INPUT).click()
    browser.find_element(*AdminPage.PRODUCT_NAME_INPUT).clear()
    browser.find_element(*AdminPage.PRODUCT_NAME_INPUT).send_keys("Headphones Samsung")
    browser.find_element(*AdminPage.META_TAG_TITLE_INPUT).click()
    browser.find_element(*AdminPage.META_TAG_TITLE_INPUT).clear()
    browser.find_element(*AdminPage.META_TAG_TITLE_INPUT).send_keys("Headphones Samsung")
    browser.find_element(*AdminPage.DATA_TAB).click()
    browser.find_element(*AdminPage.MODEL_INPUT).click()
    browser.find_element(*AdminPage.MODEL_INPUT).clear()
    browser.find_element(*AdminPage.MODEL_INPUT).send_keys("Galaxy Buds Pro")
    browser.find_element(*AdminPage.SAVE_PRODUCT_BUTTON).click()
    browser.find_element(*AdminPage.SUCCESS_ALERT)
    time.sleep(3)  # для демо


def test_delete_product_admin_page(browser, login_admin_page):
    wait = WebDriverWait(browser, 3)
    browser.find_element(*AdminPage.CATALOG_MENU).click()
    wait.until(EC.visibility_of_element_located(AdminPage.PRODUCTS_PANEL))
    browser.find_element(*AdminPage.PRODUCTS_PANEL).click()
    browser.find_element(*AdminPage.PRODUCT_CHECKBOX).click()
    browser.find_element(*AdminPage.PRODUCT_TRASH).click()
    wait.until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
    browser.find_element(*AdminPage.SUCCESS_ALERT)
    time.sleep(3)  # для демо


def test_register_new_user(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(*RegisterAccountPage.FIRST_NAME_INPUT).click()
    browser.find_element(*RegisterAccountPage.FIRST_NAME_INPUT).clear()
    browser.find_element(*RegisterAccountPage.FIRST_NAME_INPUT).send_keys("Ivan")
    browser.find_element(*RegisterAccountPage.LASTNAME_INPUT).click()
    browser.find_element(*RegisterAccountPage.LASTNAME_INPUT).clear()
    browser.find_element(*RegisterAccountPage.LASTNAME_INPUT).send_keys("Ivanov")
    browser.find_element(*RegisterAccountPage.EMAIL_INPUT).click()
    browser.find_element(*RegisterAccountPage.EMAIL_INPUT).clear()
    browser.find_element(*RegisterAccountPage.EMAIL_INPUT).send_keys("ivanov@mail.ru")
    browser.find_element(*RegisterAccountPage.TELEPHONE_INPUT).click()
    browser.find_element(*RegisterAccountPage.TELEPHONE_INPUT).clear()
    browser.find_element(*RegisterAccountPage.TELEPHONE_INPUT).send_keys("+79992223344")
    browser.find_element(*RegisterAccountPage.PASSWORD_INPUT).click()
    browser.find_element(*RegisterAccountPage.PASSWORD_INPUT).clear()
    browser.find_element(*RegisterAccountPage.PASSWORD_INPUT).send_keys("qwerty1")
    browser.find_element(*RegisterAccountPage.CONFIRM_PASSWORD_INPUT).click()
    browser.find_element(*RegisterAccountPage.CONFIRM_PASSWORD_INPUT).clear()
    browser.find_element(*RegisterAccountPage.CONFIRM_PASSWORD_INPUT).send_keys("qwerty1")
    browser.find_element(*RegisterAccountPage.PRIVACY_POLICY_CHECKBOX).click()
    browser.find_element(*RegisterAccountPage.CONTINUE_BUTTON).click()
    time.sleep(3)  # для демо


def test_switch_currency(browser):
    browser.get(browser.url)
    browser.find_element(*MainPage.CURRENCY_FORM).click()
    browser.find_element(*MainPage.POUND_CURRENCY).click()
    browser.find_element(*MainPage.CURRENCY_FORM).click()
    browser.find_element(*MainPage.EURO_CURRENCY).click()
    browser.find_element(*MainPage.CURRENCY_FORM).click()
    browser.find_element(*MainPage.US_CURRENCY).click()
