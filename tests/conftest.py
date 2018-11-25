import pytest
import logging

from base.browser_manager import WebDriverManager

@pytest.fixture(scope='session')
def browser_type(self):
    return "chrome"

@pytest.fixture(scope='session')
def run_browser(browser_type):
    driver = WebDriverManager(browser_type)
    driver = driver.get_browser_type()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)  # TODO: consider of a correct level
    return logger
