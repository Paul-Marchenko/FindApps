from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOption

from pages.urls import main_url


class WebDriverManager:

    def __init__(self, browser):
        self.browser = browser

    def get_browser_type(self):
        if self.browser == "iexplorer":
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "edge":
            driver = webdriver.Edge(EdgeDriverManager().install())
        elif self.browser == "firefox":
            #driver = webdriver.Firefox()
            driver = webdriver.Firefox(GeckoDriverManager().install())
        elif self.browser == "safari":
            driver = webdriver.Safari()
        elif self.browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            # chrome_option = ChromeOption()
            # webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
            #driver_instance = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
            #webdriver.Chrome(executable_path=ChromeDriverManager().install())
        else:
            raise ValueError("Incorrect browser name")
        driver.implicitly_wait(3)
        # driver.maximize_window()
        driver.get(main_url())
        return driver



