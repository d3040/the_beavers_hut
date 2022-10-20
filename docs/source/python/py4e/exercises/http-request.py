# HTTP Request in Python
'''
import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mySock.send(cmd)

while True:
	data = mySock.recv(535)
	if (len(data) < 1):
		break
	print(data.decode())

mySock.close()
'''
# Simplest HTTP Request in Python
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # https://d3040.com

for line in fhand:
	print(line.decode().strip())

'''
'''
#using beautifulsoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	print(tag.get('href', None))
'''
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
'''
'''
# Ex 12.1

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certicicate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_1226874.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
sum_of_values = 0

#Retrieve all of the span tags
tags = soup('span')
for tag in tags:
	# Look at the content of a tag
	sum_of_values += int(tag.contents[0])

print(sum_of_values)
'''

# Ex 12.2

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#url = 'http://py4e-data.dr-chuck.net/known_by_Areej.html'
url = 'https://tld-list.com/tlds-from-a-z'
count = int(input('Enter count: '))
position_x = int(input('Enter position: ')) - 1
sequence_of_names = ['Areej'] #['Fikret']

for n in range(count):
	print('Retrieving:', url)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	# Retrieve anchor at position x
	url = tags[position_x].get('href', None)
	sequence_of_names.append(tags[position_x].contents[0])

print('Sequence of names:', sequence_of_names)
print('Last name in sequence:', sequence_of_names[-1])
