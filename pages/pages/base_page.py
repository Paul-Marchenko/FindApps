import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from pages.urls import main_url
from tests.conftest import logger


#@pytest.mark.usefixtures("logger")
class BasePage:
    def __init__(self, driver=None, url=""):
        self.driver = driver
        self.url = main_url

    def open_page(self):
        self.driver.get_url(self.url)
        #logger.info("Page with url " + self.url + " is opened.")

    def get_title(self):
        title = self.driver.title
        #logger.info("Title is " + title)
        return title

    def wait_for_element(self, locator,
                         locator_type=By.XPATH,
                         timeout=10,
                         poll_frequency=1
                         ):
        wait = WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def get_element(self, locator='', locator_type=By.XPATH):
        element = self.wait_for_element(locator, locator_type)
        #logger.info(element + " is selected")
        return element

    def select_page(self, locator='', locator_type=By.XPATH):
        page = self.get_element(locator, locator_type)
        page.click()
        #logger.info("Page " + page + " is selected.")

    def clear_field(self, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        element.clear()

    def send_data(self, data, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        element.send_keys(data)
        #logger.info("Data " + data + " is send")

    def element_select(self, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)
        element.click()
        #logger.info(element + " is selected")

    def verify_current_url(self):
        current_url = self.driver.current_url
        #logger.info("Current url" + " is " + current_url)
        return current_url

    def is_element_displayed(self, locator='', locator_type=By.XPATH):
        #import pdb; pdb.set_trace()
        element = self.get_element(locator, locator_type)
        element = element.is_displayed()
        #logger.info(element + " is displayed")
        return element

    def is_element_present(self, locator='', locator_type=By.XPATH):
        element = self.get_element(locator, locator_type)

