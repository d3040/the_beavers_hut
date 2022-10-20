import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1226877.json'
data = urllib.request.urlopen(url, context=ctx).read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)

sum_counts = 0
for comment in info["comments"]:
    sum_counts += int(comment["count"])

print(sum_counts) 