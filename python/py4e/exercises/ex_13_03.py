import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1226876.xml'
data = urllib.request.urlopen(url, context=ctx).read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')

sum_counts = 0
for count in counts:
    sum_counts += int(count.text)

print(sum_counts) 