import pytest
import logging

from base.browser_manager import WebDriverManager


# @pytest.fixture(scope='session')
# def browser_type():
#     #return "chrome"
#     return "firefox"


@pytest.fixture(scope='session')
def run_browser(browser):
    driver = WebDriverManager(browser)
    driver = driver.get_browser_type()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
#@pytest.fixture()
def logger():
    log = logging.getLogger("pytest-logger")
    log.setLevel(logging.DEBUG)  # TODO: consider of a correct level
    log.debug('INIT logger')
    return log


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--type_test")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def type_test(request):
    return request.config.getoption("--type_test")
