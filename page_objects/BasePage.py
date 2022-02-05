import logging
from selenium.common.exceptions import TimeoutException
import allure
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.actions = ActionChains(driver)
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.driver.test_name}.log"))
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step("Выполняется клик по элементу {locator}")
    def click_element(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)
        element.click()

    @allure.step("Ввод '{value} в поле {locator}'")
    def input(self, locator, value):
        self.logger.info("Input {} in input {}".format(value, locator))
        find_field = self.wait.until(EC.presence_of_element_located(locator))
        find_field.click()
        find_field.clear()
        find_field.send_keys(value)

    def check_element_presence(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)

    def go_to_page(self, url):
        self.driver.get(url)
