import pytest

from pages.pages.main_page.main_page import MainPage
from pages.pages.job_page.job_page import JobPage
from pages.urls import JOBS_URN, POSITION_URN
from tests.conftest import *
from pages.locators.main_page_locators import *
from pages.locators.job_page_locators import *


class TestMainPage:

    def test_job_page(self, run_browser):
        main_page = MainPage(run_browser)
        main_page.select_job_page(JOB_LINK)
        current_url = main_page.verify_current_url()
        assert current_url == JOBS_URN

    def test_selected_vacancies(self, run_browser):
        job_page = JobPage(run_browser)
        job_page.select_vacancy(POSITION)
        current_url = job_page.verify_current_url()
        assert current_url == POSITION_URN
