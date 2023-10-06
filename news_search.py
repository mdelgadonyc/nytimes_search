import logging
import requests
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error


def convert_date(dateStr):
    day, month, year = dateStr.split()
    monthDict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
                 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    month = monthDict[month]

    return f'{year}-{month}-{day}'


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connect to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')

# Obtain NYTimes RSS Feed
nytRSSUrl = 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml'

# Fetch the given url using requests;
page = requests.get(nytRSSUrl)
logging.debug("status code: " + str(page.status_code))

connection = create_connection("nyt_sqlitedb")

create_china_table = """
    CREATE TABLE IF NOT EXISTS china_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        link TEXT NOT NULL,
        date TEXT NOT NULL
    );
"""


if page.status_code == requests.codes.ok:
    # Parse the XML with BeautifulSoup 
    soup = BeautifulSoup(page.text, "xml")

    execute_query(connection, create_china_table)

    create_articles = """
    INSERT INTO
        china_table (title, link, date)
    VALUES"""

    # Locate all RSS feed items mentioning China
    items = soup.find_all('item')
    for item in items:
        if 'china' in item.title.text.lower():
            create_articles += f"('{item.title.text}', '{item.link.text}', '{convert_date(item.pubDate.text[5:16])}'),"

    create_articles = create_articles[:-1] + ';'

    execute_query(connection, create_articles)

select_articles = "SELECT * from china_table"
articles = execute_read_query(connection, select_articles)

for article in articles:
    print(article)
