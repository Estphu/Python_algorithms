from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import re

url = 'https://interactive.aljazeera.com/aje/2018/live-results-pakistan-election-day-2018/index.html'
# Get the path to the downloaded EdgeDriver executable
edge_driver_path = EdgeChromiumDriverManager().install() + '.exe'

# Specify the path to the Microsoft Edge binary
edge_binary_path = '/path/to/microsoft-edge-binary'  # Replace with the actual path

# Set up Edge options
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = edge_binary_path

driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path), options=edge_options)  # You might need to adjust the path or use another driver

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

        # Extract border color from the style attribute
        border_color_match = re.search(r'box-shadow:\s*([^;]+)', content['style'])
        match = re.search(r'box-shadow:[^;]+(\b\w+)', content['style'])
        
        if border_color_match:
            election_dict[constituency_id]['border_color'] = border_color_match.group(1)
            election_dict[constituency_id]['color'] = match.group(1)

    print(election_dict)

finally:
    # Close the browser window
    driver.quit()