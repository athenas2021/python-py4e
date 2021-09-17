import urllib.request, urllib.parse, urllib.error
import json
import ssl

   # serviceurl = 'http://py4e-data.dr-chuck.net/json?'
serviceurl = 'http://py4e-data.dr-chuck.net/comments_1344221.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = serviceurl

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print(len(js['comments']))
i = 0
count = 0
while i < len(js['comments']):
  count += int(js['comments'][i]['count'])
  i += 1

print(count)
