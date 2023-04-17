import logging
import requests
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connect to SQLite DB succuessful")
    except Error as e:
        print(f"The error '{e}' occured")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

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

connection = create_connection("nyt_sqlitedb")

create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        nationality TEXT
    );
"""

execute_query(connection, create_users_table)

create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""

execute_query(connection, create_posts_table)

create_comments_table = """
    CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
    );
"""

create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
    );
"""

execute_query(connection, create_comments_table)
execute_query(connection, create_likes_table)
