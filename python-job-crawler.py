import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from careerPages import careerPages

# Store your keywords in a txt file where every word is on a new line
FILENAME = "keywords.txt"
keywords = []
with open(FILENAME) as f:
    for keyword in f.readlines():
        keywords.append(keyword.strip())

def close_dialogs(driver):
    for selector in ['.close-button', '.close']:
        try:
            close_button = driver.find_element(By.CSS_SELECTOR, selector)
            close_button.click()
            break  # Stop after clicking the first found dialog
        except Exception:
            continue

def crawl_careerPage(url, driver):
    driver.get(url)
    
    try:
        # Wait for the body element to be present—indicating that the page has loaded.
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as error:
        print(f"Error loading {url}: {error}")
        return False

    # Once the page is loaded, close any dialogs that might appear.
    close_dialogs(driver)

    # Process the page content
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page_text = soup.get_text().lower()
    found_keywords = {keyword for keyword in keywords if keyword.lower() in page_text}
    if found_keywords:
        print(f'💃 Found keyword "{", ".join(found_keywords)}" at {url}')
        return True
    else:
        return False

def main():
    print("🏁 Starting the web crawler...")
    start_time = time.time()

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Disable loading images, extensions, and GPU to speed up page loads
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")

    # Automatically install the correct ChromeDriver version
    driver_path = ChromeDriverManager().install()
    # Adjust the path if it ends with THIRD_PARTY_NOTICES.chromedriver
    if driver_path.endswith("THIRD_PARTY_NOTICES.chromedriver"):
        driver_dir = os.path.dirname(driver_path)
        driver_path = os.path.join(driver_dir, "chromedriver")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    keywords_found_count = 0
    for careerPage in careerPages:
        if crawl_careerPage(careerPage, driver):
            keywords_found_count += 1
        time.sleep(1)  # Delay between requests

    driver.quit()
    print(f"📜 Keywords were found in {keywords_found_count} out of {len(careerPages)} career pages.")
    elapsed_time = time.time() - start_time
    print(f"⏱️ Web crawler finished in {elapsed_time:.2f} seconds.")
    print("💤 Web crawler has finished.")

if __name__ == '__main__':
    main()
