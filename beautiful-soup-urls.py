
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url - ')
count = int(input('Enter Count - '))
position = int(input('Enter Position - '))

if url == '':
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

i = 0
print(url)
while i < count:

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    #for tag in tags:

    print(tags[position-1].get('href', None))
    url = tags[position-1].get('href', None)
    i +=1
