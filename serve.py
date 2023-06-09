from flask import Flask
from markupsafe import escape
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def heart_flask():
    return "<p>Thanks for visiting!</p>"


@app.route('/china')
def china_articles():
    article_entries = ""

    connection = create_connection("nyt_sqlitedb")

    select_articles = "SELECT * from china_table"
    articles = execute_read_query(connection, select_articles)

    for article in articles:
        article_entries += article[1] + '<br>'

    return article_entries

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

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


