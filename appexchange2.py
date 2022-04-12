import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException
from bs4 import BeautifulSoup
import pandas
import requests
import time
import csv
import re



PATH = ('/Users/mac/Desktop/Programming/Environments/Chromedriver/chromedriver')

link = "https://appexchange.salesforce.com/appxstore?type=App"

with webdriver.Chrome(PATH) as driver:
    driver.get(link)

    datalist = []

    try:
        show_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"appx-load-more-button-id']")))
        #show_more.click()
        driver.execute_script("arguments[0].click();",show_more)
    
    except TimeoutException:
        driver.quit()

    except StaleElementReferenceException:

        driver.quit()


    for elem in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"appx-tile appx-tile-app tile-link-click"))):
        data = [item.text for item in elem.find_elements_by_class("appx-tile-content-el")]
        datalist.append(data)

df = pandas.DataFrame(datalist)
print(df)




