import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from careerPages import careerPages

# Store your keywords in a txt file where every word is on a new line
FILENAME = "keywords.txt"
keywords = []
with open(FILENAME) as f:
    for keyword in f:
        keywords.append(keyword.strip())

def close_dialogs(driver):
    for selector in ['.close-button', '.close']:
        try:
            driver.find_element(By.CSS_SELECTOR, selector).click()
            break
        except WebDriverException:
            continue

def crawl_careerPage(url, driver):
    try:
        driver.set_page_load_timeout(20)
        driver.get(url)
    except WebDriverException as e:
        err_msg = str(e)
        if 'ERR_NAME_NOT_RESOLVED' in err_msg:
            print(f"❌ Skipping unreachable domain: {url}")
        else:
            print(f"❌ Skipping {url}: {e.__class__.__name__}: {err_msg}")
        return False
    except Exception as e:
        print(f"❌ Skipping {url}: unexpected error: {e}")
        return False

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except Exception as error:
        print(f"Error loading {url}: {error}")
        return False

    close_dialogs(driver)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page_text = soup.get_text().lower()
    found_keywords = [kw for kw in keywords if kw.lower() in page_text]
    if found_keywords:
        print(f'💃 Found keyword "{", ".join(found_keywords)}" at {url}')
        return True
    return False

def main():
    print("🏁 Starting the web crawler...")
    start_time = time.time()

    # Chrome options for headless, no-gpu, no images, etc.
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    # Install ChromeDriver and ensure it's executable
    driver_path = ChromeDriverManager().install()
    if driver_path.endswith("THIRD_PARTY_NOTICES.chromedriver"):
        driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver")
    try:
        os.chmod(driver_path, os.stat(driver_path).st_mode | 0o111)
    except Exception:
        pass

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    keywords_found_count = 0
    for url in careerPages:
        try:
            if crawl_careerPage(url, driver):
                keywords_found_count += 1
        except Exception:
            print(f"❌ Unexpected error on {url}, skipping.")
        time.sleep(1)

    driver.quit()
    print(f"📜 Keywords were found in {keywords_found_count} out of {len(careerPages)} career pages.")
    print(f"⏱️ Web crawler finished in {time.time() - start_time:.2f} seconds.")
    print("💤 Web crawler has finished.")

if __name__ == '__main__':
    main()
