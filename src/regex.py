from __future__ import print_function, division

__author__ = 'amrit'

import sys
import glob, os
import re, unicodedata
import urllib2
from bs4 import BeautifulSoup
import tldextract
import indexer
sys.dont_write_bytecode = True

strings = ['http://www.confirm-paypal.com/', 'http://www.google.com/', 'https://www.hud.ac.uk/students/',
           'http://www.iphonesticker.com/js/x10.html']

# 1 represents phishing and -1 is good.

def punctuate_preproc(x):
    return re.sub(r"<(.*?)>|\n|(\\(.*?){)|}|[#!$%^&*()_+|~\^\-<>/={}\[\],:\";<>?,.\/\\]|[@]", ' ', x)


def pref_suffix(response='', str=''):
    if re.match(r'(https?://)?\w*.?\w*\-\w*.?\w*/?', str):
        return 1
    else:
        return -1


def multi_subdomain(response='', str=''):
    pattern = re.compile(r'https?://((\w*.)*)/?')
    print(pattern.findall(str))
    domain = pattern.findall(str)[0][0]
    li = re.split('\.', domain)
    if 'www' in li:
        li.remove('www')

    if 0 <= len(li) <= 2:
        return -1
    elif len(li) == 3:
        return 0
    else:
        return 1


## Need to incorporate age in this.
def SSH(response='', str=''):
    pattern = re.compile(r'(https?)://')
    domain = pattern.findall(str)[0]
    li = re.split('\.', domain)
    if 'https' in li:
        return -1
    else:
        return 1


def request_url(response='', str=''):
    soup = BeautifulSoup(response, 'html.parser')
    url = tldextract.extract(str)
    total = 0
    no = 0
    list = soup.find_all('img', attrs={'src': re.compile("^https?://")}) + soup.find_all('audio', attrs={
        'src': re.compile("^https?://")}) + soup.find_all('video', attrs={'src': re.compile("^https?://")})
    print(list)
    for l in list:
        total += 1
        ext = tldextract.extract(l['src'])
        if ext.domain != url.domain and re.compile("^https?://").match(l)!=None:
            no += 1
    print(total, no)
    try:
        frac = no / total
    except:
        frac = 0
    if frac < 0.22:
        return -1
    elif 0.22 <= frac <= 0.61:
        return 0
    else:
        return 1


def url_anchor(response='', str=''):
    soup = BeautifulSoup(response, 'html.parser')
    url = tldextract.extract(str)
    total = 0
    no = 0
    for l in soup.find_all('a', attrs={'href': re.compile("^https?://")}):
        total += 1
        ext = tldextract.extract(l['href'])
        if ext.domain != url.domain and re.compile("^https?://").match(l)!=None:
            no += 1
    print(total, no)
    try:
        frac = no / total
    except:
        frac = 0
    if frac < 0.31:
        return -1
    elif 0.31 <= frac <= 0.67:
        return 0
    else:
        return 1


def links_in_tags(response='', str=''):
    soup = BeautifulSoup(response, 'html.parser')
    url = tldextract.extract(str)
    total = 0
    no = 0
    list = [unicodedata.normalize('NFKD', l['href']).encode('ascii','ignore') for l in soup.find_all('link', attrs={'href': re.compile("^https?://")})] + \
           [unicodedata.normalize('NFKD', l['src']).encode('ascii','ignore') for l in soup.find_all( 'script', attrs={'src': re.compile("^https?://")})] + [
        unicodedata.normalize('NFKD', l['content']).encode('ascii', 'ignore') for l in soup.find_all('meta', attrs={'content': re.compile("^https?://")})]
    print(list)
    for l in list:
        total += 1
        ext = tldextract.extract(l)
        if ext.domain != url.domain and re.compile("^https?://").match(l)!=None:
            no += 1
    print(total, no)
    try:
        frac = no / total
    except:
        frac = 0
    if frac < 0.17:
        return -1
    elif 0.17 <= frac <= 0.81:
        return 0
    else:
        return 1

def SFH(response='', str=''):
    soup = BeautifulSoup(response, 'html.parser')
    url = tldextract.extract(str)
    list = [unicodedata.normalize('NFKD', l['action']).encode('ascii','ignore') for l in soup.find_all('form')]
    for l in list:
        if l=='' or l=='about:blank':
            return 1
    for l in list:
        ext = tldextract.extract(l)
        if ext.domain != url.domain and re.compile("^https?://").match(l)!=None:
            return 0
    return -1

def google_index(response='', str=''):
    return indexer.index(response,str)

# most steps need to be in specific order to achieve one
def process(response, str, *steps):
    l = []
    request = urllib2.Request(strings[0].lower())
    response = urllib2.urlopen(request).read()
    for p in steps:
        l.append(p(response, str))
    return l

if __name__ == '__main__':
    str = strings[1].lower()
    request = urllib2.Request(str)
    response = urllib2.urlopen(request).read()
    # l=process(response,str,pref_suffix,multi_subdomain,SSH,request_url,url_anchor,links_in_tags,SFH,google_index)

    print(google_index(response, str))

## More other link sources.

# <a href=url>
# <applet codebase=url>
# <area href=url>
# <base href=url>
# <blockquote cite=url>
# <body background=url>
# <del cite=url>
# <form action=url>
# <frame longdesc=url> and <frame src=url>
# <head profile=url>
# <iframe longdesc=url> and <iframe src=url>
# <img longdesc=url> and <img src=url> and <img usemap=url>
# <input src=url> and <input usemap=url>
# <ins cite=url>
# <link href=url>
# <object classid=url> and <object codebase=url> and <object data=url> and <object usemap=url>
# <q cite=url>
# <script src=url>
# HTML 5 adds a few (and HTML5 seems to not use some of the ones above as well):
#
# <audio src=url>
# <button formaction=url>
# <command icon=url>
# <embed src=url>
# <html manifest=url>
# <input formaction=url>
# <source src=url>
# <video poster=url> and <video src=url>
# These aren't necessarily simple URLs:
#
# <img srcset="url1 resolution1 url2 resolution2">
# <source srcset="url1 resolution1 url2 resolution2">
# <object archive=url> or <object archive="url1 url2 url3">
# <applet archive=url> or <applet archive=url1,url2,url3>
# <meta http-equiv="refresh" content="seconds; url">
# SVGs can also contain links to resources: <svg><image href="url" /></svg>
#
# In addition, the style attribute can contain css declarations with one or several urls. For example: <div style="background: url(image.png)">
