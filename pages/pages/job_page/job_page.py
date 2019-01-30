from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from pages.pages.base_page import BasePage
from pages.locators.job_page_locators \
    import ALL_CATEGORIES_DROP_DOWN, SEARCH_FIELD, SEARCH_BUTTON
from pages.urls import JOBS_URN


class JobPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(url=JOBS_URN)

    def select_vacancy(self, position):

        element = self.get_element(ALL_CATEGORIES_DROP_DOWN,
                                   locator_type=By.NAME)
        select = Select(element)
        position_type = self.get_element(position).text
        select.select_by_value(position_type)

    def select_town(self, town_name):
        self.element_select(town_name)
        import time;
        time.sleep(2)

    def input_town(self, town_name):
        self.send_data(town_name, SEARCH_FIELD, locator_type=By.CSS_SELECTOR)

    def click_search_button(self):
        self.element_select(SEARCH_BUTTON, locator_type=By.CSS_SELECTOR)

