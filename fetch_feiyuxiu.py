#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from HTMLParser import HTMLParser
import urllib2, urllib
import re
import os, glob

def remove_existing_mp3():
    for fl in glob.glob("*.mp3"):
        os.remove(fl)

def parseProgramPage(url):
    response = urllib2.urlopen(url)
    html = response.read()
    
    m = re.search('http://mod.cri.cn/eng/ez/morning(.*).mp3', html)
    mp3_url = m.group(0)
    filename = os.path.basename(mp3_url)
    if not os.path.isfile(filename):
        remove_existing_mp3()
        print("Downloading " + mp3_url)
        urllib.urlretrieve (mp3_url, filename)
        print("Finished")
    else:
        print("File {0} exists.".format(filename))
            

# create a subclass and override the handler methods
class FeiyuxiuHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.isInsideInterviewList = 0;
    
    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for name, value in attrs:
                if name == 'class' and value == 'interviewlist':
                    self.isInsideInterviewList = 1
        if self.isInsideInterviewList and tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    url = 'http://english.cri.cn' + value
                    parseProgramPage(url)
            self.isInsideInterviewList = 0
                  
            

response = urllib2.urlopen('http://english.cri.cn/easyfm/easymorning.html')
html = response.read()

# instantiate the parser and fed it some HTML
parser = FeiyuxiuHTMLParser()
parser.feed(html)

