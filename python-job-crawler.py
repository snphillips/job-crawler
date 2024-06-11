from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# List of websites to crawl
websites = [
    'https://adhoc.rec.pro.ukg.net/ADH1000ADHOC/JobBoard/1893bc9c-1fe2-4c48-90e8-0de36fe3f2b2/?q=&o=postedDateDesc',
    'https://nationbuilder.com/careers#apply',
    'https://jobs.ashbyhq.com/kaizenlabs',
    'https://www.fastly.com/about/careers/current-openings/',
    'https://watershed.com/careers',
    'https://jobs.jobvite.com/tylertech/jobs',
    'https://skylight.digital/careers/join/#open-positions',
    'https://cleargov.applytojob.com/apply/',
    'https://www.gethearth.com/careers/',
    'https://civicactions.com/careers/#open-positions',
    'https://rematter.com/careers/#ashby_embed',
    'https://join.tts.gsa.gov/',
    'https://boards.greenhouse.io/accela',
    'https://readme.com/careers',
    'https://oddball.io/jobs/',
    'https://bowery.co/join-us/?location=new-york&department=technology',
    # Add more websites as needed

    # TODO: Crawler doesn't work on the sites below. Figure out why
    'https://up.codes/careers',
]

# Keywords to search for
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
        # Example: Close a dialog by clicking on a close button
        close_button = driver.find_element(By.CSS_SELECTOR, '.close-button')
        if close_button:
            close_button.click()
    except Exception as e:
        pass  # No dialog to close or unable to find the close button

def crawl_website(url, driver):
    driver.get(url)
    time.sleep(5)  # Wait for initial load

    close_dialogs(driver)  # Handle any potential dialogs

    try:
        # Wait for page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as e:
        print(f"Error loading {url}: {e}")
        return False

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page_text = soup.get_text().lower()  # Convert page text to lowercase
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
    chrome_options.add_argument('--headless')  # Run headless Chrome
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    keywords_found_count = 0
    for website in websites:
        if crawl_website(website, driver):
            keywords_found_count += 1
        time.sleep(2)  # Add a delay between requests

    driver.quit()
    print(f"Keywords were found in job listings at {keywords_found_count} out of {len(websites)} websites.")
    print(f"💤 Web crawler has finished.")
