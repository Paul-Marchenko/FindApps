import pytest
import allure

from pages.pages.main_page.main_page import MainPage
from pages.pages.job_page.job_page import JobPage
from pages.urls import JOBS_URN, POSITION_URN
from tests.conftest import *
from pages.locators.main_page_locators import *
from pages.locators.job_page_locators import *


class TestMainPage:

    @pytest.allure.step("Test first")
    def test_job_page(self, run_browser, logger):
        main_page = MainPage(run_browser)
        main_page.select_job_page(JOB_LINK)
        current_url = main_page.verify_current_url()
        assert current_url == JOBS_URN
        logger.info("Page with url " + current_url + " is opened")

    @pytest.allure.step('My Feature')
    def test_selected_vacancies(self, run_browser, logger):
        job_page = JobPage(run_browser)
        job_page.select_vacancy(POSITION)
        current_url = job_page.verify_current_url()
        assert current_url == POSITION_URN
        logger.info("Job_page with url " + current_url + " is opened")
