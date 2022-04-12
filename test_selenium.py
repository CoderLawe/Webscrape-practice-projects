import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException
from bs4 import BeautifulSoup
import requests
import time
import csv
import re


PATH = ('/Users/mac/Desktop/Programming/Environments/Chromedriver/chromedriver')

driver = webdriver.Chrome(PATH)


driver.get('https://techwithtim.net/')

link = driver.find_element_by_link_text('Python Programming')
link.click()

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials'))
    )
    element.click()

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'sow-button-19310003'))
    )
    element.click()
    
    

except:
    driver.quit()