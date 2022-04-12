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


source = requests.get('https://appexchange.salesforce.com/appxstore?type=App').text

driver.get('https://appexchange.salesforce.com/appxstore?type=App')

soup = BeautifulSoup(source, 'lxml')

csv_file = open('Appexchange.csv','w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['App Name','Company','Date Released','Category','Price','Image URL'])

#print(soup.prettify())

while True:
    try:
        showmore=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID ,'appx-load-more-button-id')))
        showmore.click()
    except TimeoutException:
        break
    except StaleElementReferenceException:
        break
               
               

    for card in soup.find_all('a', class_='appx-tile appx-tile-app tile-link-click'):

        #print(card)

        title = card.find('span', class_='appx-tile-content-el').text

        #print(title.text)

        date = card.find('span', class_='appx-tile-content-el-value').text

        #print(date.text)

        company = card.find('span', class_='appx-tile-feature appx-tile-feature-provider').text

        #print(company.text)

        categories = card.find('span', class_='appx-tile-content-el-value-category').text

        #print(categories.text)

        price = soup.find('span', class_='appx-tile-feature-price').text
        #print(price.text)

        rating = card.find('span', class_='appx-rating-stars').text
        #print (rating.text)

        image_src = card.find('img', class_='appx-tile-content-el')['data-src']

        

    # print(image_src)
        #for title in soup.find_all('span', class_='appx-tile-content-el'):

        print(title)

        #https://partners.salesforce.com/servlet/servlet.FileDownload?file=00P3A00000V4VYQUA3

    csv_writer.writerow([title,company,date,categories,price, image_src])

csv_file.close()

