import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')

# Obtain NYTimes RSS Feed
nytRSSUrl = 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml'

# Fetch the given url using requests;
page = requests.get(nytRSSUrl)
logging.debug("status code: " + str(page.status_code))

if page.status_code == requests.codes.ok:
    # Parse the XML with BeautifulSoup 
    soup = BeautifulSoup(page.text, "xml")
    
    # Retrieve all titles mentioning China
    titles = soup.find_all('title')
    for title in titles:
        if 'china' in title.text.lower():
            print(title.text)
