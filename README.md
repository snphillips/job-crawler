# python-job-crawler

Looking for work stinks. Scouring websites for job postings is time-consuming and repetitive. This Python-based web crawler is designed to visit a list of specified online career pages that and search for specific keywords, in my case, for front-end related jobs.

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

## Running the Script

Using the terminal, run the script:

```
python3 python-job-crawler.py
```
The script will start and print messages indicating the progress, including which websites were crawled and whether any keywords were found.

