#encoding:utf-8

import urllib

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

def getCourseStatistics():
    pass

def getStudentStatistics():
    pass

def getAllCourseInfo(departmentId):
    pass

