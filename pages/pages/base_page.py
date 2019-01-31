from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.urls import MAIN_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = MAIN_URL

    def open_page(self):
        self.driver.get_url(self.url)

    def get_title(self):
        title = self.driver.title
        return title

    def wait_for_element(self, locator,
                         locator_type=By.XPATH,
                         timeout=10,
                         poll_frequency=1
                         ):
        wait = WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency)
        element = wait.until(EC.element_to_be_clickable((locator_type,
                                                         locator)))
        return element

    def get_element(self, locator='', locator_type=By.XPATH):
        print("log11")
        element = self.wait_for_element(locator, locator_type)
        print("log121")
        print("log0000")
        return element

    def select_page(self, locator='', locator_type=By.XPATH):
        page = self.get_element(locator, locator_type)
        page.click()

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

    def is_element_displayed(self, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        element = element.is_displayed()
        return element

    def is_element_present(self, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        return element

