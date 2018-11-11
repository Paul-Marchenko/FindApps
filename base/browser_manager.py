from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverManager:

    def __init__(self, browser):
        self.browser = browser

    def get_browser_type(self):
        webdriver.Chrome(executable_path=ChromeDriverManager().install())


