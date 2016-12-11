#!/usr/bin/python2

import xml.etree.ElementTree as ET
import urllib2
import urllib
import sys

import threading
import ssl

def main():
    # TODO: Is opener thread safe?
    opener = urllib2.build_opener()

    opener.addheaders = [('User-agent', 'igoturuseragentrighthere')]

    response = opener.open('http://en.wikipedia.org/wiki/' + sys.argv[1])
    html_file = open('wiki.html', 'w')
    html_file.write(response.read())
    html_file.close()
    root = ET.parse('wiki.html').getroot()

    for link in root.findall(".//*[@class='references'].//*a"):
        if link.get('href').startswith('http'):
            test_ref(opener, link)

def test_ref(opener, link):
    t = threading.Thread(target=do_test, args=(opener, link,))
    t.start()

def do_test(opener, link):
    try:
        opener.open(link.get('href'), timeout=5)
    except Exception as error:
        #print link.get('href') + ": " + str(error)
        print link.get('href')

if __name__ == '__main__':
    main()
