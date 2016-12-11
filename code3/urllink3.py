# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

todo = list()
visited = list()
url = input('Enter - ')
todo.append(url)

while len(todo) > 0:
    print("====== Todo list count is ", len(todo))
    url = todo.pop()

    if (not url.startswith('http')):
        print("Skipping", url)
        continue

    if (url.find('facebook') > 0):
        continue

    if (url in visited):
        print("Visited", url)
        continue

    print("===== Retrieving ", url)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    visited.append(url)

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        newurl = tag.get('href', None)
        if (newurl is not None):
            todo.append(newurl)
