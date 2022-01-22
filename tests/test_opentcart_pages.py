from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def test_product_macbook(browser):
    browser.get(browser.url + "/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("MacBook"))
    wait.until(EC.visibility_of_element_located(ProductPage.PRODUCT_AREA))
    wait.until(EC.visibility_of_element_located(ProductPage.THUMBNAILS))
    wait.until(EC.element_to_be_clickable(ProductPage.BUTTON_CART))
    wait.until(EC.text_to_be_present_in_element(ProductPage.BUTTON_CART, "Add to Cart"))


def test_login_page_external(browser):
    browser.get(browser.url + "/admin")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_USERNAME))
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_PASSWORD))
    wait.until(EC.visibility_of_element_located(LoginPage.SUBMIT_BUTTON))
    wait.until(EC.visibility_of_element_located(LoginPage.OPENCART_LINK))
    wait.until(EC.visibility_of_element_located(LoginPage.FORGOTTEN_PASSWORD))


def test_register_account(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.CONTENT))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.PERSONAL_DETAILS_AREA))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.YOUR_PASSWORD_HEADER))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.REGISTER_LINK))


def test_catalog(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(CategoryPage.CATEGORY_PAGE))
    wait.until(EC.visibility_of_element_located(CategoryPage.COLUMN_LEFT))
    wait.until(EC.element_to_be_clickable(CategoryPage.LIST_VIEW_BUTTON))
    wait.until(EC.element_to_be_clickable(CategoryPage.GRID_VIEW_BUTTON))
    wait.until(EC.text_to_be_present_in_element(CategoryPage.PRODUCT_COMPARE_LINK, "Product Compare"))
