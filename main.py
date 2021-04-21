# wellstar-public.conservation_web_scrape

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/Users/redacted/Downloads/chromedriver_win32/chromedriver.exe')
wellstar_url = 'https://wellstar-public.conservation.ca.gov/Well/Well/Index'  #
driver.get(wellstar_url)
locator = '//*[@id="WellGrid"]/div[3]/a[3]/span'
a = input('ready?')

while a == 'y':
    driver.find_element_by_xpath(locator).click()
    a = input('ready?')
