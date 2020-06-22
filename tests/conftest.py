import pytest
import logging

from base.browser_manager import WebDriverManager
from utils.test_data import BROWSERS_MAIN, TEST_BRO, BROWSERS


# @pytest.fixture(scope='session')
# def browser_type():
#     return "firefox"


@pytest.fixture(scope='session')
def run_browser(run_type):
    for browser in BROWSERS:
        driver = WebDriverManager(browser)
        if run_type == 'local':
            driver = driver.get_local_browser_type()
        elif run_type == 'remote':
            driver = driver.get_remote_browser_type()
        else:
            raise ValueError("Incorrect runtype of browser")
        yield driver
        driver.quit()


@pytest.fixture(scope='session')
def logger():
    log = logging.getLogger("pytest-logger")
    log.setLevel(logging.DEBUG)  # TODO: consider of a correct level
    log.debug('INIT logger')
    return log


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--type_test")
    parser.addoption("--run_type")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
#
#
# @pytest.fixture(scope="session")
# def type_test(request):
#     return request.config.getoption("--type_test")

@pytest.fixture(scope="session")
def run_type(request):
    return request.config.getoption("--run_type")
