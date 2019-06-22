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
        print("log1")
        self.select_page(town_name)
        print("log1331")
        import time;
        time.sleep(2)
        print("log14441")

    # def wait_for_element(self, locator,
    #                      locator_type=By.XPATH,
    #                      timeout=10,
    #                      poll_frequency=1
    #                      ):
    #     wait = WebDriverWait(self.driver,
    #                          timeout=timeout,
    #                          poll_frequency=poll_frequency)
    #     element = wait.until(EC.element_to_be_clickable((locator_type,
    #                                                      locator)))
    #     return element

    def input_town(self, town_name):
        self.send_data(town_name, SEARCH_FIELD, locator_type=By.CSS_SELECTOR)

    def click_search_button(self):
        self.element_select(SEARCH_BUTTON, locator_type=By.CSS_SELECTOR)

