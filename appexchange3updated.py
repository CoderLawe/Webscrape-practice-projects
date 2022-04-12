from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC


def get_field_text_if_exists(item, selector):
    """Extracts a field by a CSS selector if exists."""
    try:
        return item.find_element_by_class_name(selector).text
    except NoSuchElementException:
        return ""


def get_link_if_exists(item, selector):
    """Extracts an href attribute value by a CSS selector if exists."""
    try:
        return item.find_element_by_css_selector(selector).get_attribute("href")
    except NoSuchElementException:
        return ""

PATH = ('/Users/mac/Desktop/Programming/Environments/Chromedriver/chromedriver')

driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 30)

driver.get("https://appexchange.salesforce.com/appxstore?type=App")

#location = driver.find_element_by_css_selector('.partnerLocation input')
#location.clear()
#location.send_keys("Colorado, USA")

# select the first suggestion from a suggestion dropdown
#dropdown_suggestion = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul[id^=typeahead] li a')))
#dropdown_suggestion.click()

# click more until no more results to load
while True:
    try:
        more_button = wait.until(EC.visibility_of_element_located((By.ID, 'appx-load-more-button-id'))).send_keys('\n')
    except TimeoutException:
        break

# wait for results to load
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'appx-tiles-grid')))

# parse results
for result in driver.find_elements_by_class_name('appx-tiles-grid'):
    name = get_field_text_if_exists(result, 'appx-tile-content-el')
    company = get_field_text_if_exists(result, 'appx-tile-feature appx-tile-feature-provider')
    date = get_field_text_if_exists(result, 'appx-tile-content-el-value')
   # website = get_link_if_exists(result, 'a[ng-if*=website]')

    print(name, company, date)

driver.quit()
#main-content > div > div.content-maxWid > div > div.finder-tool-root.ng-scope > div.row.match-your-search.filter-result > div.row.seclection-result > div.row.resel-cat-selection.ng-scope > div:nth-child(1) > div.col-xs-12.col-sm-9.col-md-10.padding0 > h2 > a
