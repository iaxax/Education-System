#encoding:utf-8

from xml.etree import ElementTree

def xmlToResultInfo(resultXml):
    root = ElementTree.fromstring(resultXml).text
    return (root[0].text, root[1].text)

def xmlToCourseInfo(courseXml):
    root = ElementTree.fromstring(courseXml)
    result = []
    for child in root:
        result.append((
            child[0].text, child[1].text, child[2].text, child[3].text,
            child[4].text, child[5].text, child[6].text
        ))
    return result