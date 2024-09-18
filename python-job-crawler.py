import time
import logging
from pathlib import Path
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from careerPages import careerPages
from chromeDriverPath import chromeDriverPath


logging.basicConfig(  # logger initialization
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SRC_KW_FILENAME = "keywords.txt"  # file containing keywords to look for
PAGE_LOADING_TIME_SLEEPER = 5  # time in s waiting for the web page to load

def main() -> None:
    """
    Main function to initialize the web crawler, configure the Chrome driver,
    and crawl career pages.

    Raises:
        FileNotFoundError: If file `SRC_KW_FILENAME` is not found.
        IOError: If there is an issue opening or reading the file.
        Exception: Any other exceptions that may occur during file processing.
    """

    file_path = Path(SRC_KW_FILENAME)
    keywords = []

    # If the kw file exists, insert its kws inside our keywords list
    if file_path.exists():
        try:
            with file_path.open('r', encoding='utf-8') as f:
                keywords = [keyword.strip().lower() for keyword in f if keyword.strip()]
        except (IOError, FileNotFoundError) as e:
            logging.error(f"Error reading {SRC_KW_FILENAME}: {e}")
    if not keywords:
        logging.error("No keywords to search for. Please check your keywords file.")
        return

    logging.info("🏁 Starting the web crawler...")

    # Setup Chrome options
    chrome_options = Options()
    options_list = ['--headless', '--no-sandbox', '--disable-dev-shm-usage']
    for opt in options_list:
        chrome_options.add_argument(opt)

    # Initialize WebDriver using ChromeDriverManager
    service = Service(chromeDriverPath)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Get the number of match
    kws_found_count = 0
    for careerPage in careerPages:
        if crawl_careerPage(careerPage, driver, keywords):
            kws_found_count += 1
        time.sleep(1)

    driver.quit()
    logging.info(f"Keywords were found in job listings at {kws_found_count} out of {len(careerPages)} career pages.")


def close_dialogs(driver: webdriver.Chrome) -> None:
    """
    Tries to close any potential pop-up dialogs that may appear on the page.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance used for browsing.

    Returns:
        None
    """
    try:
        # Modify the CSS selector to find common close buttons, adjust as needed
        close_button = WebDriverWait(driver, PAGE_LOADING_TIME_SLEEPER).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.close-button, .close'))
        )
        if close_button:
            close_button.click()
            logging.info("Closed a dialog on the page.")
    except TimeoutException:
        logging.debug("No dialog found to close.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


def crawl_careerPage(url: str, driver: webdriver.Chrome, kws: List[str]) -> bool:
    """
    Crawls a given career page URL to search for keywords in the job listings.

    Args:
        url (str): URL of the career page to visit.
        driver (webdriver.Chrome): Selenium WebDriver instance used for browsing.
        kws (List[str]): the kws to look for on page at URL

    Returns:
        bool: True if any keywords were found on the page, False otherwise.
    """
    logging.info(f"Visiting career page: {url}")

    driver.get(url)  # Selenium is loading url page

    # Wait for the page to load completely using WebDriverWait before moving on
    try:
        WebDriverWait(driver, PAGE_LOADING_TIME_SLEEPER).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except Exception as error:
        logging.error(f"Error loading {url}: {error}")
        return False

    # Handle any potential dialogs after the page loads
    close_dialogs(driver)

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page_text = soup.get_text().lower()

    # Search for keywords in the page text
    found_keywords = {kw for kw in kws if kw.lower() in page_text}

    if found_keywords:
        logging.info(f'💃 Found keywords {", ".join(found_keywords)} in job listings at {url}')
    else:
        logging.info(f'No keywords found in job listings at {url}')

    return bool(found_keywords)

if __name__ == '__main__':
    main()
