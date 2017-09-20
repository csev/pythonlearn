import os
import urllib.request, urllib.parse, urllib.error

print('Please enter a URL like http://data.pr4e.org/cover3.jpg')
urlstr = input().strip()
img = urllib.request.urlopen(urlstr)

# Get the last "word"
words = urlstr.split('/')
fname = words[-1]

# Don't overwrite the file
if os.path.exists(fname):
    if input('Replace ' + fname + ' (Y/n)?') != 'Y':
        print('Data not copied')
        exit()
    print('Replacing', fname)

fhand = open(fname, 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied to', fname)
fhand.close()
