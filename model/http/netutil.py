#encoding:utf-8
import urllib

def get(url):
    f = urllib.urlopen(url)
    return f.read()

def post(url, data):
    param = urllib.urlencode(data)
    f = urllib.urlopen(url, param)
    return f.read()