# python-job-crawler

This project is a Python-based web crawler designed to visit a list of career pages and search for specific job keywords. The script leverages Selenium and BeautifulSoup to scrape job listings from various websites and identify positions that match your keywords.

## About
This web crawler was developed with the assistance of ChatGPT, with some prompts and guidance provided by me.

## Prerequisites
Python 3.11.1
Google Chrome
ChromeDriver
Installation
Install Python 3
If you don't have Python 3 installed, you can download and install it from the official Python website.

##Create a Virtual Environment (Optional but Recommended)
Creating a virtual environment is recommended to manage dependencies:

Create a Virtual Environment:

python3 -m venv venv
This command creates a directory named venv which contains a standalone Python installation.

Activate the Virtual Environment:

On macOS and Linux:


source venv/bin/activate
On Windows:


.\venv\Scripts\activate
Install Dependencies:

With the virtual environment activated, install the necessary Python packages:

bash
pip install selenium webdriver_manager beautifulsoup4
Deactivate the Virtual Environment:

When you are done working in the virtual environment, deactivate it:


deactivate
Setup ChromeDriver
Download and install the ChromeDriver that matches your Chrome version. You can do this automatically using the webdriver_manager package.

## Create careerPages.py
Create a file named `careerPages.py` in the same directory as your script. This file should contain the list of websites you want to crawl. Add this file to your .gitignore to prevent it from being included in version control.

Example careerPages.py

# careerPages.py

careerPages = [
    'https://great-company/careers',
    'https://we-value-work-life-balance.com/jobs',
    'https://not-making-the-world-a-worse-place.com/joinus',
    # Add more websites as needed
]

## Running the Script
Ensure you have your virtual environment activated (if you created one).

Run the script:

```
python3 job-crawler.py
```
The script will start and print messages indicating the progress, including which websites were crawled and whether any keywords were found.

