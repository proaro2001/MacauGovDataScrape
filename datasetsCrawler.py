"""
This file is used to crawl the datasets from the https://data.gov.mo/Datasets
It looks for the title, publisher, last update time, file type, tags, and the
link to access the page of the dataset.

This crawler will not crawl the datasets but only gather a list of datasets.
"""

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = "https://data.gov.mo/Datasets"
ua = UserAgent()
headers = {"User-Agent": ua.random}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

    #links_download
    next_page = soup.find("a", id="links_download")
    print(next_page)
    
else:
    print("Error occurred! Status code: ", response.status_code)