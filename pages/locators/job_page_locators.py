from constants import city_name

######################################################################################################################
# JOB Page Locators
######################################################################################################################
SEARCH_FIELD = '.job'  # CSS locator
SEARCH_BUTTON = '.btn-search'  # CSS locator

######################################################################################################################
# Categories Locators
######################################################################################################################
ALL_CATEGORIES_DROP_DOWN = 'category'  # NAME locator
POSITION = '//option[text()="QA"]'  # XPATH locator

######################################################################################################################
# Towns Locators
######################################################################################################################
TOWN1 = '//div[@class="b-region-filter"]//ul[2]/li[1]'  # XPATH locator
TOWN = '(//a[contains(@href,"https://jobs.dou.ua/vacancies/?city")])[1]'  # XPATH locator
HEADER_VACANCY = '//ul[@class="other"]//li[1]'  # XPATH locator
HEADER_VACANCY1 = '//div[@class="b-inner-page-header"]//h1[contains(text(),"{city_name}")]'  # XPATH locator
