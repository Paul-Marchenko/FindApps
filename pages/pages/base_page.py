from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.urls import main_url


class BasePage:
    def __index__(self, driver=None, url=""):
        self.driver = driver
        self.url = main_url

    def open_page(self):
        self.driver.get_url(self.url)

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, locator,
                         locator_type=By.XPATH,
                         timeout=10,
                         poll_frequency=1
                         ):
        wait = WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency)
        element = wait.until(EC.element_to_be_clickable((locator, locator_type)))
        return element

    def get_element(self, locator='', locator_type=By.XPATH):
        element = self.wait_for_element(locator, locator_type)
        return element

    def clear_field(self, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        element.clear()

    def send_data(self, data, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        element.send_keys(data)

    def element_select(self, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        element.click()

    def verify_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def is_element_dispalyed(self, locator='', locator_type=By.XPATH):
        pass
