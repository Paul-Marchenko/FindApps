import datetime
import pytest

from pages.pages.main_page.main_page import MainPage
from pages.pages.job_page.job_page import JobPage
from pages.urls import JOBS_URN, POSITION_URN, CITY_URN
from pages.locators.main_page_locators import JOB_LINK
from pages.locators.job_page_locators import POSITION, HEADER_VACANCY, TOWN
from base.base_actions import take_screenshot


@pytest.fixture
def generate_name():
    yield datetime.datetime.now().isoformat


class TestMainPage:

    @pytest.mark.sanity
    def test_job_page(self, run_browser, logger, generate_name):
        main_page = MainPage(run_browser)
        main_page.select_job_page(JOB_LINK)
        current_url = main_page.verify_current_url()
        assert current_url == JOBS_URN
        logger.info("Page with url " + current_url + " is opened")
        name = '%.*s' % (19, generate_name())
        take_screenshot(run_browser, name)

    @pytest.mark.smoke
    def test_selected_vacancies(self, run_browser, logger, generate_name):
        job_page = JobPage(run_browser)
        job_page.select_vacancy(POSITION)
        current_url = job_page.verify_current_url()
        print(current_url)
        assert current_url == POSITION_URN
        logger.info("Job_page with url " + current_url + " is opened")
        name = '%.*s' % (19, generate_name())
        take_screenshot(run_browser, name)

    @pytest.mark.feature
    def test_vacancies_for_town_displayed(self,
                                          run_browser,
                                          logger,
                                          generate_name):
        job_page = JobPage(run_browser)
        job_page.select_vacancy(POSITION)
        import pdb; pdb.set_trace()
        job_page.select_town(TOWN)
        #job_page.click_search_button()
        vacancies = job_page.is_element_displayed(HEADER_VACANCY)
        print(vacancies)
        assert vacancies == True
        current_url = job_page.verify_current_url()
        expected_url = CITY_URN + r'[0-9a-zA-Zа-яА-я]+'
        #assert current_url == expected_url
        name = '%.*s' % (19, generate_name())
        take_screenshot(run_browser, name)
        logger.info("Vacancies for town" + " is displayed")
