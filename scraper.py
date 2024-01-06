from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = 'https://interactive.aljazeera.com/aje/2018/live-results-pakistan-election-day-2018/index.html'

# Set up the Selenium WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # You might need to adjust the path or use another driver

try:
    # Load the page
    driver.get(url)

    # Wait for the tab content to be present (adjust the timeout as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'provincial-tab-content'))
    )

    # Get the page source after JavaScript execution
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    
    election_dict = {}
    
    for content in soup.find_all('div', class_='constituency-card'):

        constituency_id = content.find('h2', class_ = 'constituency-card__id').get_text()

        election_dict[constituency_id] = {
            'id': constituency_id,
            'name': content.find('h3', class_ = 'constituency-card__name').get_text(),
            'voters': content.find('div', class_ = 'constituency-card__reg-voters').get_text(),
            'winner': content.find('div', class_ = 'constituency-card__candidate-name').get_text(),
        }

        for value in content.find_all('div', class_ = 'constituency-card__label'):
            if 'TURNOUT' in value.get_text():
                election_dict[constituency_id]['turnout'] = value.get_text().replace('TURNOUT','')
            if 'POLLED' in value.get_text():
                election_dict[constituency_id]['polled_votes'] = value.get_text().replace('VOTES POLLED','')
            elif 'VOTES' in value.get_text():
                election_dict[constituency_id]['votes'] = value.get_text().replace('VOTES','')

    print(election_dict)

finally:
    # Close the browser window
    driver.quit()