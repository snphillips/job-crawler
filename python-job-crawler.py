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
from chromeDriverPath import chromeDriverPath

# Store your keywords in a txt file where every word is on a new line
FILENAME = "keywords.txt" 

keywords =[]
with open(FILENAME) as f:
    for keyword in f.readlines():
        keywords.append(keyword.strip())
def main():
    print("🏁 Starting the web crawler...")

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver with the exact path to chromedriver
    # Add your specific path to a filed called chromeDriverPath.py.
    # The contents of chromeDriverPath.py should look similar to this:
    # chromeDriverPath = '/Users/sueellenmisky/.wdm/drivers/chromedriver/mac64/129.0.6668.70/chromedriver-mac-x64/chromedriver'
    # Ensure chromeDriverPath.py is in your .gitignore
    service = Service(chromeDriverPath)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    keywords_found_count = 0
    for careerPage in careerPages:
        if crawl_careerPage(careerPage, driver):
            keywords_found_count += 1
        # Add a delay between requests
        time.sleep(1)  

    driver.quit()
    print(f"📜 Keywords were found in {keywords_found_count} out of {len(careerPages)} career pages.")
    print(f"💤 Web crawler has finished.")

def close_dialogs(driver):
    try:
        # If there's a dialog box with a close button with class .close-button or .close
        # Add more class names as you encounter them
        close_button = driver.find_element(By.CSS_SELECTOR, '.close-button' | '.close')
        if close_button:
            close_button.click()
    except Exception as e:
        # No dialog to close or unable to find the close button
        pass

def crawl_careerPage(url, driver):
    driver.get(url)
    time.sleep(5)  # Wait for initial load

    # Handle any potential dialogs
    close_dialogs(driver)

    try:
        # Wait for page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as error:
        print(f"Error loading {url}: {error}")
        return False

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Convert page text to lowercase to make search case-agnostic
    page_text = soup.get_text().lower()
    found_keywords = set()
    for keyword in keywords:
        if keyword.lower() in page_text:
            found_keywords.add(keyword)
    if found_keywords:
        print(f'💃 Found keyword "{", ".join(found_keywords)}" at {url}')
        return True
    else:
        # If you want to see the pages that DON'T have keywords, enable the next line
        # print(f'No keywords found at {url}')
        return False

if __name__ == '__main__':
    main()
