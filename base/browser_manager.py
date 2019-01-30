from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager

from pages.urls import MAIN_URL


class WebDriverManager:

    def __init__(self, browser):
        self.browser = browser

    def get_browser_type(self):
        if self.browser == "iexplorer":
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "edge":
            driver = webdriver.Edge(EdgeDriverManager().install())
        elif self.browser == "firefox":
            # TODO: use driver = webdriver
            # .Firefox(GeckoDriverManager().install())
            driver = webdriver\
                .Firefox(executable_path='/Users/pavel/'
                                         '.wdm/geckodriver/'
                                         'v0.23.0/macos/geckodriver')
        elif self.browser == "safari":
            driver = webdriver.Safari()
        elif self.browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            # TODO: impelement different chrome_option
            # chrome_option = ChromeOption()
            # webdriver.Chrome(ChromeDriverManager().
            # install(), chrome_options=chrome_option)
            #driver_instance = webdriver.Chrome(ChromeDriverManager()
            # .install(), chrome_options=chrome_option)
        else:
            raise ValueError("Incorrect browser name")
        driver.implicitly_wait(3)
        # TODO: impelement driver features driver.maximize_window()
        driver.get(MAIN_URL)
        return driver



