#encoding:utf-8

import urllib
from src.config.netcfg import wsdlUrl

def get(url):
    f = urllib.urlopen(url)
    textbytes = f.read()
    text = textbytes.decode('utf8')
    return text

def post(url, data):
    param = urllib.urlencode(data)
    f = urllib.urlopen(url, param)
    textbytes = f.read()
    text = textbytes.decode('utf8')
    return text
