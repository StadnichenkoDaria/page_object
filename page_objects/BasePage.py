import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        # self.actions = ActionChains(driver)
        # self.__config_logger()

    # def __config_logger(self):
    #     self.logger = logging.getLogger(type(self).__name__)
    # self.logger.addHandler(logging.FileHandler(f"logs/{self.driver.test_name}.log"))
    # self.logger.setLevel(level=self.driver.log_level)

    def click_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.click()

    def input(self, locator, value):
        # self.logger.info("Input {} in input {}".format(value, locator))
        find_field = self.wait.until(EC.presence_of_element_located(locator))
        find_field.click()
        find_field.clear()
        find_field.send_keys(value)

    def check_element_presence(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def go_to_page(self, url):
        self.driver.get(url)



