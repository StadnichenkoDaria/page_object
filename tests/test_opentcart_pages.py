import allure
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
    browser.get(browser.url + ProductPage.PRODUCT_PAGE)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("MacBook"))
    wait.until(EC.visibility_of_element_located(ProductPage.PRODUCT_AREA))
    wait.until(EC.visibility_of_element_located(ProductPage.THUMBNAILS))
    wait.until(EC.element_to_be_clickable(ProductPage.BUTTON_CART))
    wait.until(EC.text_to_be_present_in_element(ProductPage.BUTTON_CART, "Add to Cart"))


def test_visible_elements_login_page_external(browser):
    browser.get(browser.url + AdminPage.ADMIN_PAGE)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_USERNAME))
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_PASSWORD))
    wait.until(EC.visibility_of_element_located(LoginPage.SUBMIT_BUTTON))
    wait.until(EC.visibility_of_element_located(LoginPage.OPENCART_LINK))
    wait.until(EC.visibility_of_element_located(LoginPage.FORGOTTEN_PASSWORD))


def test_visible_elements_register_account(browser):
    browser.get(browser.url + RegisterAccountPage.REGISTER_PAGE)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.CONTENT))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.PERSONAL_DETAILS_AREA))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.YOUR_PASSWORD_HEADER))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(RegisterAccountPage.REGISTER_LINK))


def test_visible_elements_catalog(browser):
    browser.get(browser.url + CategoryPage.CATEGORY_PAGE)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(CategoryPage.CATEGORY_AREA))
    wait.until(EC.visibility_of_element_located(CategoryPage.COLUMN_LEFT))
    wait.until(EC.element_to_be_clickable(CategoryPage.LIST_VIEW_BUTTON))
    wait.until(EC.element_to_be_clickable(CategoryPage.GRID_VIEW_BUTTON))
    wait.until(EC.text_to_be_present_in_element(CategoryPage.PRODUCT_COMPARE_LINK, "Product Compare"))


@allure.title('Добавление товара в раздел разминистратора')
def test_add_new_product_admin_page(browser, url):
    login_page = LoginPage(browser)
    admin_page = AdminPage(browser)
    login_page.login_admin_page(url)
    admin_page.go_to_product_page()
    admin_page.add_new_product("Headphones Samsung", "Headphones Samsung", "Galaxy Buds Pro")
    admin_page.check_alert_msg()


@allure.title('Удаление товара из раздела разминистратора')
def test_delete_product_admin_page(browser, url):
    wait = WebDriverWait(browser, 3)
    login_page = LoginPage(browser)
    admin_page = AdminPage(browser)
    login_page.login_admin_page(url)
    admin_page.go_to_product_page()
    admin_page.delete_product()
    wait.until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
    admin_page.check_alert_msg()


@allure.feature('Registration')
@allure.title('Регистрация нового пользователя')
def test_register_new_user(browser, url):
    register_page = RegisterAccountPage(browser)
    browser.get(browser.url + RegisterAccountPage.REGISTER_PAGE)
    register_page.create_user(register_page.DEFAULT_FIRST_NAME,
                              register_page.DEFAULT_LAST_NAME,
                              register_page.DEFAULT_EMAIL,
                              register_page.DEFAULT_PHONE_NUMBER,
                              register_page.DEFAULT_PASSWORD,
                              register_page.DEFAULT_PASSWORD)
    register_page.privacy_policy_accept()
    register_page.click_continue()


@allure.title('Переключение валют')
def test_switch_currency(browser):
    main_page = MainPage(browser)
    browser.get(browser.url)
    main_page.switch_to_euro()
    main_page.switch_to_usd()
    main_page.switch_to_pound()
