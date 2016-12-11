#! /bin/sh

rm *.pyc */*.pyc
mv gmane/mapping.sqlite gmane/mapping.save
rm *.sqlite */*.sqlite
mv gmane/mapping.save gmane/mapping.sqlite
rm *.zip

zip -r geodata.zip geodata
zip -r gmane.zip gmane
zip -r pagerank.zip pagerank
zip -r tracks.zip tracks
zip -r roster.zip roster
zip -r bs4.zip bs4

