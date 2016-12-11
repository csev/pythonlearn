# Note - this code must run in Python 2.x and you must download
# http://www.py4e.com/code/BeautifulSoup.py
# Into the same folder as this program

import string
import sqlite3
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

conn = sqlite3.connect('wikidata.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS TinyTable (id INTEGER PRIMARY KEY,
                   url TEXT, page BLOB, retrieved_at timestamp)''')


# A slightly extended dictionary
class sash(dict):
    def sortvalues(self, reverse=True):
        return sorted(list(self.items()),
                      key=lambda x: (x[1], x[0]), reverse=reverse)


def tinyTable(url):
    global cur, conn
    cur.execute('''SELECT id, page, retrieved_at
                   FROM TinyTable WHERE URL = ?''', (url, ))
    try:
        row = cur.fetchone()
        print('DATE', row[2])
        return row[1]
    except:
        row = None
    print('Retrieving', url)

    data = urllib.request.urlopen(url).read()
    if row is not None:
        cur.execute('''UPDATE TinyTable SET page=?,
                    retrieved_at=datetime('now')
                    WHERE id=?''', (str(data, 'utf-8'), row[0]))
    else:
        cur.execute('''INSERT INTO TinyTable (url, page, retrieved_at)
                    VALUES (?, ?, datetime('now'))''',
                    (url, str(data, 'utf-8')))
    conn.commit()
    return data

cururl = 'https://ctools.umich.edu/portal/tool/27500dea-c105-4f7b-a195-3c89536a64b7?pageName=%2Fsite%2Ff57681b8-6db9-46cf-aad1-3a0bdd621138%2Fhome&action=view&panel=Main&realm=%2Fsite%2Ff57681b8-6db9-46cf-aad1-3a0bdd621138'
prefix = 'https://ctools.umich.edu/portal/tool/27500dea-c105-4f7b-a195-3c89536a64b7'

urls = list()
urls.append(cururl)
visited = list()
editcounts = sash()
postcounts = sash()

while len(urls) > 0:
    print('=== URLS Yet To Retrieve:', len(urls))
    cururl = urls.pop()
    if cururl in visited: continue
    print('RETRIEVING', cururl)
    data = tinyTable(cururl)
    visited.append(cururl)
    soup = BeautifulSoup(data)
    tags = soup('a')
    # print 'Tags'
    for tag in tags:
        print(tag)
        url = tag.get('href', None)
        if url is None: continue
        # Don't follow absolute urls
        if not url.startswith(prefix): continue
        newurl = urllib.basejoin(cururl, url)
        if newurl in visited: continue
        # print 'APPENDING', newurl
        if newurl.find('action=view') > 0 or newurl.find('action=history') > 0:
            urls.append(newurl)

print('EDITS:')
for (key, val) in editcounts.sortvalues():
    print(key, val)

for (key, val) in sorted(postcounts.items()):
    print(key, val)

conn.close()
