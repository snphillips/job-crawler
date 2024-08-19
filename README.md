# Python Job Web Crawler

Looking for work stinks. Scouring websites for job postings is time-consuming and repetitive. This Python-based web crawler is designed to visit a list of specified online career pages that and search for specific keywords, in my case, for front-end related jobs.

This web crawler was developed with ChatGPT, with prompts and guidance provided by me.

note: This script is not perfect. Confirm that it works on your list of urls by first using keywords that do appear on the sites you're searching.

## Getting Started

### Prerequisites
- Python3: https://www.python.org/downloads/
- Google Chrome
- ChromeDriver: https://developer.chrome.com/docs/chromedriver/get-started

### Installation
Clone the repo and navigate into the directory:

```
git clone https://github.com/yourusername/job-keyword-web-crawler.git
cd job-keyword-web-crawler
```

Install the necessary Python libraries:
```
pip3 install selenium webdriver_manager beautifulsoup4
```

### Create careerPages.py
The list of career pages to visit is stored in `careerPages.py`.
Create a file named `careerPages.py` in the same directory as your script. 

```
touch careerPages.py
```

This file contain the list of websites you want to crawl. 

Below is a sample `careerPages.py`. Replace the placeholder urls with your own list.

```
careerPages = [
    'https://great-company.com/careers',
    'https://we-value-work-life-balance.com/jobs',
    'https://not-making-the-world-a-worse-place.com/joinus',
    'https:/bird-watching-and-forest-bathing.com/openings'
    # Add more websites as needed
]
```

If you'd like to keep your list of career pages to yourself, confirm that the file has been added to your `.gitignore` to prevent it from being included in version control.

### Create chromeDriverPath.py

This script expects you to include the direct path to your chromedriver.
```
touch chromeDriverPath.py
```

Below is a sample `chromeDriverPath.py`. Replace the path to your chromedriver with your own path.
```
chromeDriverPath = '/Users/davidpuddy/.wdm/drivers/chromedriver/mac64/127.0.6533.119/chromedriver-mac-x64/chromedriver'
```

## Running the Script

Ensure your 'chromedriver' is running.
To run chromedriver directly from the command line, follow these steps:

Locate chromedriver:
webdriver-manager downloads chromedriver to a specific directory. By default, it's usually stored in your home directory under .wdm.

Navigate to the directory:
Open your terminal and navigate to the directory containing the chromedriver executable (the file path below is an example only).
```
cd /Users/newman/.wdm/drivers/chromedriver/mac64/127.0.6533.119/chromedriver-mac-x64/
```

Ensure the chromedriver file has executable permissions. You can set the correct permissions using the chmod command.
```
chmod +x chromedriver
```

Execute the chromedriver executable directly from the terminal.
```
./chromedriver
```

Now that the chromedriver is running, using the terminal, run the script:

```
python3 python-job-crawler.py
```
The script will start and print messages indicating the progress, including which websites were crawled and whether any keywords were found.

