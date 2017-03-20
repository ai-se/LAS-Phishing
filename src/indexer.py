from __future__ import print_function, division

__author__ = 'amrit'

import sys
# Google says don't use this script: https://twitter.com/methode/status/783733724655517696
# This script is a violation of Google Terms of Service. Don't use it.

import requests
from bs4 import BeautifulSoup
from urllib import urlencode
sys.dont_write_bytecode = True

proxies = {
    'https' : 'https://192.168.1.1:8080',
    'https' : 'http://192.168.1.1:8080'
    }

def index(response='',line=''):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    headers = {'User-Agent': user_agent}
    query = {'q': 'info:' + line}
    google = "https://www.google.com/search?" + urlencode(query)
    data = requests.get(google, headers=headers)
    data.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(str(data.content), "html.parser")
    try:
        check = soup.find(id="rso").find("div").find("div").find("h3").find("a")
        href = check['href']
        return -1
    except AttributeError:
        return 1
