import pytest

from pages.pages.main_page.main_page import MainPage
from pages.pages.job_page.job_page import JobPage
from pages.urls import JOBS_URN, POSITION_URN
from pages.locators.main_page_locators import JOB_LINK
from pages.locators.job_page_locators import POSITION, HEADER_VACANCY,TOWN


class TestMainPage:

    @pytest.mark.sanity
    def test_job_page(self, run_browser, logger):
        main_page = MainPage(run_browser)
        main_page.select_job_page(JOB_LINK)
        current_url = main_page.verify_current_url()
        assert current_url == JOBS_URN
        logger.info("Page with url " + current_url + " is opened")

    @pytest.mark.smoke
    def test_selected_vacancies(self, run_browser, logger):
        job_page = JobPage(run_browser)
        job_page.select_vacancy(POSITION)
        current_url = job_page.verify_current_url()
        print(current_url)
        assert current_url == POSITION_URN
        logger.info("Job_page with url " + current_url + " is opened")

    @pytest.mark.feature
    def test_vacancies_for_town_displayed(self, run_browser, logger):
        job_page = JobPage(run_browser)
        job_page.select_vacancy(POSITION)
        #import pdb; pdb.set_trace()
        job_page.select_town(TOWN)
        #job_page.input_town(" ")
        import time; time.sleep(2)
        job_page.click_search_button()
        vacancies = job_page.is_element_displayed(HEADER_VACANCY)
        print(vacancies)
        assert vacancies == True
        logger.info("Vacancies for town" + " is displayed")