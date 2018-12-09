from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from pages.pages.base_page import BasePage
from pages.locators.job_page_locators import *
from pages.urls import JOBS_URN


class JobPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(url=JOBS_URN)

    def select_vacancy(self, position):

        element = self.get_element(ALL_CATEGORIES_DROP_DOWN, locator_type=By.NAME)
        select = Select(element)
        position_type = self.get_element(POSITION).text
        select.select_by_value(position_type)
