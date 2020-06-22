from .driver import WebDriver

with WebDriver() as driver:
    driver.login()