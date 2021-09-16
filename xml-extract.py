import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/comments_1344220.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = serviceurl #+ urllib.parse.urlencode()
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
count = 0
total = 0
while count < len(results):
  total += int(results[count].find('count').text)
  count += 1
#lng = results[0].find('geometry').find('location').find('lng').text
#location = results[0].find('formatted_address').text

#print('lat', lat, 'lng', lng)
print(total)
