#!/usr/bin/python2

import xml.etree.ElementTree as ET
import urllib2
import urllib
import sys

def main():
    opener = urllib2.build_opener()
    #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    opener.addheaders = [('User-agent', 'igoturuseragentrighthere')]
    #response = opener.open('http://en.wikipedia.org/wiki/Big_Table')
    response = opener.open('http://en.wikipedia.org/wiki/' + sys.argv[1])
    html_file = open('wiki.html', 'w')
    html_file.write(response.read())
    html_file.close()
    root = ET.parse('wiki.html').getroot()
    #print root.findall("*[@class='references']")
    for link in root.findall(".//*[@class='references'].//*a"):
        if link.get('href').startswith('http'):
            try:
                opener.open(link.get('href'))
            except urllib2.URLError as e:
                print link.get('href')

if __name__ == '__main__':
    main()
