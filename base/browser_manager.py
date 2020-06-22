import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ChromeOptions, FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


from pages.urls import MAIN_URL
from utils.helpers import chrome_driver_path


class WebDriverManager:

    def __init__(self, browser):
        self.browser = browser

    def get_local_browser_type(self):
        if self.browser == "ie":
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "firefox":
            # TODO: use driver = webdriver
            driver = webdriver.Firefox(GeckoDriverManager().install())
            # driver = webdriver.Firefox(executable_path='/Users/pavel/'
            #                              '.wdm/geckodriver/'
            #                              'v0.23.0/macos/geckodriver')
        elif self.browser == "safari":
            driver = webdriver.Safari()
        elif self.browser == "chrome":
            print("os.pathsep + chrome_driver_path     ", os.pathsep + chrome_driver_path)
            os.environ["PATH"] += os.pathsep + chrome_driver_path
            # driver = webdriver.Chrome(executable_path=chrome_driver_path)
            driver = webdriver.Chrome(ChromeDriverManager().install())

        else:
            raise ValueError("Incorrect browser name")
        driver.implicitly_wait(3)
        # TODO: impelement driver features driver.maximize_window()
        driver.get(MAIN_URL)
        return driver

    def get_remote_browser_type(self):
        command_executor = 'http://localhost:4444/wd/hub'
        options = None
        driver = None
        if self.browser == "iexplorer":
            desired_capabilities = DesiredCapabilities.INTERNETEXPLORER
            print("This is IE:--------->")
        elif self.browser == "firefox":
            # TODO: use driver = webdriver
            desired_capabilities = DesiredCapabilities.FIREFOX
            options = FirefoxOptions()
            print("This is FF:--------->"'\n')
            driver = webdriver.Remote(command_executor=command_executor,
                                      options=options,
                                      desired_capabilities=desired_capabilities)
        elif self.browser == "safari":
            desired_capabilities = DesiredCapabilities.SAFARI
            print("This is SAF:--------->")
            driver = webdriver.Safari()
        elif self.browser == "chrome":
            desired_capabilities = DesiredCapabilities.CHROME
            chrome_options = ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            print("This is CH:--------->"'\n')
            driver = webdriver.Remote(command_executor=command_executor,
                                      options=chrome_options,
                                      desired_capabilities=desired_capabilities)
        else:
            raise ValueError("Incorrect browser name")
        # TODO: impelement driver features driver.maximize_window()
        desired_capabilities['os'] = "WINDOWS"
        desired_capabilities['os_version'] = "10"

        driver.implicitly_wait(3)
        driver.get(MAIN_URL)
        return driver
