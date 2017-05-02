# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

todo = list()
visited = list()
url = input('Enter - ')
todo.append(url)
count = int(input('How many to retrieve - '))

while len(todo) > 0 and count > 0 :
    print("====== To Retrieve:",count, "Queue Length:", len(todo))
    url = todo.pop()
    count = count - 1

    if (not url.startswith('http')):
        print("Skipping", url)
        continue

    if (url.find('facebook') > 0):
        continue

    if (url.find('linkedin') > 0):
        continue

    if (url in visited):
        print("Visited", url)
        continue

    print("===== Retrieving ", url)

    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print("*** Error in retrieval")
        continue

    soup = BeautifulSoup(html, 'html.parser')
    visited.append(url)

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        newurl = tag.get('href', None)
        if (newurl is not None):
            todo.append(newurl)
