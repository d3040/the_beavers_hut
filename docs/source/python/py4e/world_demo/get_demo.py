'''
World demographics:

Get the list of countries from crawling wikipedia from the link https://en.wikipedia.org/wiki/List_of_sovereign_states, updates states' information from the wiki of each state and creates a data base with the basic demographic information.

'''
import ssl
import sqlite3
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

domain = 'https://en.wikipedia.org'
url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'
# crawling foreing countries
site = urlopen(url, context=ctx)
html = site.read()
# catch error? // TBD
html_parser = BeautifulSoup(html, 'html.parser')
a_tags = html_parser.select('table>tbody>tr>td>b>a')
# create db
conn = sqlite3.connect('world_demo.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Countries
                (id INTEGER,
                name TEXT UNIQUE,
                PRIMARY KEY ("id" AUTOINCREMENT))''')

# get states
n = 0
for a in a_tags:
    country_name = a['title'] # + ' -> ' + domain + a['href'])
    # smart db update // TBD
    cur.execute('INSERT OR IGNORE INTO Countries (name) VALUES ( ? )', ( country_name, ))
    if n % 25 == 0: conn.commit()
    n += 1

