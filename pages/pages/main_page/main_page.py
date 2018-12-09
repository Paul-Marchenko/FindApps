from pages.pages.base_page import BasePage
from pages.locators.main_page_locators import *


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_job_page(self, page):
        self.select_page(page)




