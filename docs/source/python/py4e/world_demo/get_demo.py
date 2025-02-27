'''
World demographics:

Get the list of countries from crawling wikipedia from the link https://en.wikipedia.org/wiki/List_of_sovereign_states, updates states' information from the wiki of each state and creates a data base with the basic demographic information.

'''
# import modules
import re
import json
import ssl
import sqlite3
from pprint import pprint
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# functions
def initial_cleaning(phrase):
    ''' Clean general patterns '''
    # characters form crawling
    new_phrase = phrase.replace('\xa0', ' ')
    new_phrase = new_phrase.replace('\ufeff', '')
    # remove bullet
    new_phrase = new_phrase.replace('•','')
    # remove citations
    new_phrase = re.sub('\\[[0-9a-zA-Z]*\\]', '', new_phrase)
    # remove beginning and ending pipes
    new_phrase = re.sub('^\\|+|\\|+$', '', new_phrase)
    # remove duplicated pipes
    new_phrase = re.sub('\\|\\|+', '|', new_phrase)
    # trim
    new_phrase = new_phrase.strip()

    return new_phrase

def convert_label(label):
    # remove pipes
    new_label = label.replace('|', '')
    # remove dates e.g. (2024)
    #new_label = re.sub('\\((.+)\\)', '', new_label)

    return new_label

def decode_data():
    pass

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# wiki domain
domain = 'https://en.wikipedia.org'
# list of sovereing states
url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'
# crawling foreing countries
site = urlopen(url, context=ctx)
html = site.read() # get structure of page (bs4 object)
html_parser = BeautifulSoup(html, 'html.parser')
table_rows = html_parser.select('table.wikitable>tbody>tr')
# get countries info from list of sovereing states
countries = dict()
for n, row in enumerate(table_rows):
    # get data (discard headers)
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
        # save data
        countries[country] = {'url': domain + wiki_ref,  'un_membership': membership}
# get demographics
demos = dict()
for country, info in countries.items():
    demo = dict()
    url = info['url']
    site = urlopen(url, context=ctx)
    html = site.read()
    # if error found when opening page, update ERROR on page
    if site.getcode() != 200 :
        print('Error on page (' + url + '): ',document.getcode())
    # get structure of page (bs4 object)
    html_parser = BeautifulSoup(html, 'html.parser')
    table_rows = html_parser.select('table.infobox.ib-country.vcard>tbody>tr')
    # get data from wiki's country info table
    sub_level = None
    previous_label = None
    for row in table_rows:
        infobox_header = row.find('th', class_='infobox-header')
        infobox_label = row.find('th', class_='infobox-label')
        infobox_data = row.find('td', class_='infobox-data')
        infobox_img = row.find('td', class_='infobox-image')
        # tags validation
        header, label, data, flag = None, None, None, None
        if infobox_header:
            header = infobox_header.get_text('|', strip=True)
        if infobox_label:
            label = infobox_label.get_text('|', strip=True)
        if infobox_data:
            data = infobox_data.get_text('|', strip=True)
        if infobox_img:
            images = infobox_img.find_all('img')
            flag = 'https:' + re.sub('[0-9]+[p]+[x]',
                                     'width_px',
                                     images[0]['src'],
                                     flags=re.IGNORECASE)
            if len(images) > 1:
                coat_of_arms = 'https:' + re.sub('[0-9]+[p]+[x]',
                                         'width_px',
                                         images[1]['src'],
                                         flags=re.IGNORECASE)
            else:
                coat_of_arms = None
            demo['flag'] = flag
            demo['coat of arms'] = coat_of_arms
        # save country information
        if header:
            # a header sections comes with sub level labels and data
            sub_level = initial_cleaning(header)
            demo[sub_level] = dict()
        elif label and data:
            # identify if there is a bullet (item from sub level)
            if label[:1] == '•':
                bullet = True
            else:
                bullet = False
            # clear data
            label = initial_cleaning(label)
            data = initial_cleaning(data)
            # sub_level while label starts with bullet
            if bullet:
                if sub_level:
                    demo[sub_level].update({label: data})
                else:
                    # sub level not recognized
                    sub_level = previous_label
                    demo[sub_level] = dict()
                    demo[sub_level].update({label: data})
            else:
                sub_level = None
                demo[label] = data
                previous_label = label
        else:
            # do nothing, empty row...
            continue
    print(country)
    #wait = input('press any key to continue')
    demos[country] = demo
# create a json file to save
with open('country_info.json', mode='w', encoding='utf-8') as write_file:
    json.dump(demos, write_file)
'''
To Be Done:

[] clean data
[] fields histogram
[] create tables in relational data base
[] plot charts
'''

'''
info_hist = dict()
for country, info in demos.items():
    for field in info:
        info_hist[field] = info_hist.get(field, 0) + 1

pprint(info_hist)

#if label == 'Capital|and largest city':
#    demo['Capital'] = data
#    demo['Largest city'] = data
#else:
pprint(demos)
'''
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

