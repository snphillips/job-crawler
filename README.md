# python-job-crawler

Looking for work stinks. Scouring websites for jobs is time-consuming and repetitive. This Python-based web crawler is designed to visit a list of online career pages that I've specified and search for specific keywords, in my case, for front-end related jobs.

This web crawler was developed with ChatGPT, with prompts and guidance provided by me.

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
Create a file named `careerPages.py` in the same directory as your script. This file should contain the list of websites you want to crawl. Add this file to your .gitignore to prevent it from being included in version control.

Sample careerPages.py

```
careerPages = [
    'https://great-company.com/careers',
    'https://we-value-work-life-balance.com/jobs',
    'https://not-making-the-world-a-worse-place.com/joinus',
    'https:/bird-watching-and-brunch.com/openings'
    # Add more websites as needed
]
```

## Running the Script

Using the terminal, run the script:

```
python3 job-crawler.py
```
The script will start and print messages indicating the progress, including which websites were crawled and whether any keywords were found.

