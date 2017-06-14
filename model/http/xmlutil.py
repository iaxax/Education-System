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
            child.find('department_id').text, child.find('course_id').text, 
            child.find('name').text, child.find('classroom').text,
            child.find('classtime').text, child.find('type').text,
            child.find('department').text
        ))
    return result
