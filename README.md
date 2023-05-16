# nytimes_search

nytimes_search is a web scraper that searches the NYTimes RSS feed to parse and extract stories about China, storing the result in an SQLite database for later retrieval.

## Installation

Create a virtual environment for project
sudo apt install python3-venv
python3 -m venv .venv_nytimes
source  venv/bin/activate

$ pip3 install requests

# Parse the XML with BeautifulSoup
$ pip3 install beautifulsoup4
$ pip3 install lxml

# Flask handles API
$ pip3 install Flask

## Usage
Obtain NYTimes RSS Feed

# Run flask app serving titles
$ flask -app serve.py run

## Contributing

Please open an issue to suggest fixes or ideas for improving nytimes_search

## License

[The GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
