from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.urls import main_url


class WebDriverManager:

    def __init__(self, browser):
        self.browser = browser

    def get_browser_type(self):
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "safari":
            driver = webdriver.Safari()
        elif self.browser == "chrome":
            webdriver.Chrome(executable_path=ChromeDriverManager().install())
        else:
            raise ValueError("Incorrect browser name")
        driver.implicitly_wait(3)
        # driver.maximize_window()
        driver.get(main_url())
        return driver



