# python-job-crawler

This is a Python-based web crawler designed to visit a list of online career pages and search for specific keywords. The script leverages Selenium and BeautifulSoup to scrape job listings from various websites and identify positions that match your keywords.

This web crawler was developed with the assistance of ChatGPT, with prompts and guidance provided by me.

## Prerequisites
- Python3
- Google Chrome
- ChromeDriver

## Getting Started

Clone the repo and navigate into the directory.

```
git clone https://github.com/yourusername/job-keyword-web-crawler.git
cd job-keyword-web-crawler
```
## Installation

Install Python 3
If you don't have Python 3 installed, you can download and install it from the official Python website.

```
pip install selenium webdriver_manager beautifulsoup4
```

## Create careerPages.py
Create a file named `careerPages.py` in the same directory as your script. This file should contain the list of websites you want to crawl. Add this file to your .gitignore to prevent it from being included in version control.

Example careerPages.py

careerPages = [
    'https://great-company/careers',
    'https://we-value-work-life-balance.com/jobs',
    'https://not-making-the-world-a-worse-place.com/joinus',
    # Add more websites as needed
]

## Running the Script

Using the terminal, run the script:

```
python3 job-crawler.py
```
The script will start and print messages indicating the progress, including which websites were crawled and whether any keywords were found.

