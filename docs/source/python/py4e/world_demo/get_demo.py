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
# transactional dictionary
demos = dict()
# get structure of page (bs4 object)
# get countries info from list of sovereing states
html_parser = BeautifulSoup(html, 'html.parser')
table_rows = html_parser.select('table.wikitable>tbody>tr')
for n, row in enumerate(table_rows):
    # discard table headers
    country_info = row.find_all('td')
    if country_info:
        country = country_info[0].a['title']
        wiki_ref = country_info[0].a['href']
        # get UN membership
        membership = country_info[1].get_text()[2:].lower()
        if 'no membership' in membership:
            membership = 'No membership'
        elif 'un general assembly observer state' in membership:
            membership = 'UN General Assembly observer state'
        elif 'un specialized agencies' in membership:
            membership = 'UN specialized agencies'
        elif 'un member state' in membership:
            membership = 'UN member state'
        else:
            membership = 'Not specified'
        # save transaction
        demos[country] = {'url': domain + wiki_ref,  'un_membership': membership}
# get demographics
for country, info in demos.items():
    url = info['url']
    site = urlopen(url, context=ctx)
    html = site.read()
    # if error found when opening page, update ERROR on page
    if site.getcode() != 200 :
        print('Error on page (' + url + '): ',document.getcode())
    # get structure of page (bs4 object)
    html_parser = BeautifulSoup(html, 'html.parser')
    table_rows = html_parser.select('table.infobox>tbody>tr')
    fields = list()
    values = list()
    for row in table_rows:
        infobox_label = row.find('th', class_='infobox-label')
        infobox_data = row.find('td', class_='infobox-data')
        if infobox_label and infobox_data:
            field = infobox_label.get_text('|', strip=True)
            value = infobox_data.get_text('|', strip=True)
            print(field,((40 - len(field)) * ' ') + '|',value)
            wait = input('-'*120)
            #fields.append(infobox_label.get_text('|', strip=True))
            #values.append(infobox_data.get_text('|', strip=True))
    #print('Keys:\n', fields)
    #print('Values:\n', values)
    #wait = input('Press any key to continue')
'''
# TBD
# catch error? // TBD
# create db
conn = sqlite3.connect('world_demo.sqlite')
cur = conn.cursor()
cur.executescript(''''''
                CREATE TABLE IF NOT EXISTS Membership
                    (id INTEGER,
                    name TEXT UNIQUE,
                    PRIMARY KEY ("id" AUTOINCREMENT));

                CREATE TABLE IF NOT EXISTS Countries
                    (id INTEGER,
                    name TEXT UNIQUE,
                    url TEXT UNIQUE,
                    PRIMARY KEY ("id" AUTOINCREMENT));

                CREATE TABLE IF NOT EXISTS Demos
                    (id INTEGER,
                    id_country INTEGER,
                    id_un_membership INTEGER,
                    PRIMARY KEY ("id" AUTOINCREMENT),
                    FOREIGN KEY (id_un_membership) REFERENCES Membership(id));
                  '''''')
# insert country and UN membership status in db
cur.execute('INSERT OR IGNORE INTO Countries (name, url) VALUES (?, ?)', (country, wiki_ref))
cur.execute('SELECT id FROM Membership WHERE name = ?', (membership, ))
if cur.fetchone() is None:
cur.execute('INSERT INTO Membership (name) VALUES (?)', (membership, ))
cur.execute('SELECT id FROM Membership WHERE name = ?', (membership, ))
id_un_membership = cur.fetchone()[0]
cur.execute('SELECT id FROM Countries WHERE name = ?', (country, ))
id_country = cur.fetchone()[0]
 # smart db update // TBD
    if n % 25 == 0: conn.commit()
# final commit
conn.commit()
'''

