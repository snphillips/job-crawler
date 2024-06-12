from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from careerPages import careerPages

# Add your own list of keywords to search for
keywords = [
    'web developer',
    'software engineer',
    'software developer',
    'front-end',
    'frontend',
    'front end',
    'react',
    'reactjs',
    'UI Developer',
    'UI Engineer'
]

def close_dialogs(driver):
    try:
        # If there's a dialog box with a close button with the class .close-button
        close_button = driver.find_element(By.CSS_SELECTOR, '.close-button')
        if close_button:
            close_button.click()
    except Exception as e:
        # No dialog to close or unable to find the close button
        pass

def crawl_careerPage(url, driver):
    driver.get(url)
    time.sleep(5)  # Wait for initial load

    close_dialogs(driver)  # Handle any potential dialogs

    try:
        # Wait for page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as error:
        print(f"Error loading {url}: {error}")
        return False

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Convert page text to lowercase to make search case agnostic
    page_text = soup.get_text().lower()
    found_keywords = set()
    for keyword in keywords:
        if keyword.lower() in page_text:
            found_keywords.add(keyword)
    if found_keywords:
        print(f'💃 Found keywords "{", ".join(found_keywords)}" in job listings at {url}')
        return True
    else:
        print(f'No keywords found in job listings at {url}')
        return False

if __name__ == '__main__':
    print("🏁 Starting the web crawler...")

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    keywords_found_count = 0
    for careerPage in careerPages:
        if crawl_careerPage(careerPage, driver):
            keywords_found_count += 1
        # Add a delay between requests
        time.sleep(2)  

    driver.quit()
    print(f"Keywords were found in job listings at {keywords_found_count} out of {len(careerPages)} career pages.")
    print(f"💤 Web crawler has finished.")

