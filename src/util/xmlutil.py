#encoding:utf-8

from xml.etree import ElementTree
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

def xmlToResultInfo(resultXml):
    root = ElementTree.fromstring(resultXml.encode('utf-8')).text
    return (root[0], root[1])

def xmlToCourseInfo(courseXml):
    root = ElementTree.fromstring(courseXml.encode('utf-8'))
    result = []
    for child in root:
        result.append((
            child.find('department_id').text, child.find('course_id').text,
            child.find('name').text, child.find('classroom').text,
            child.find('classtime').text, child.find('type').text,
            child.find('department').text
        ))
    return result


__xml = '<?xml version="1.0" encoding="utf-8"?>'

def courseResultToXml(result):
    root = Element('result')
    success = SubElement(root, 'success')
    success.text = result['success']
    message = SubElement(root, 'message')
    message.text = result['message']
    courses = SubElement(root, 'courses')

    for c in result['courses']:
        course = SubElement(courses, 'course')
        courseId = SubElement(course, 'course_id')
        courseId.text = c['course_id']
        name = SubElement(course, 'name')
        name.text = c['name']
        classroom = SubElement(course, 'classroom')
        classroom.text = c['classroom']
        classtime = SubElement(course, 'classtime')
        classtime.text = c['classtime']
        classtype = SubElement(course, 'type')
        classtype.text = c['type']
        department = SubElement(course, 'department')
        department.text = c['department']

    return __xml + ET.tostring(root, encoding='utf-8', method='xml')

def icourseResultToXml(result):
    root = Element('result')
    success = SubElement(root, 'success')
    success.text = result['success']
    message = SubElement(root, 'message')
    message.text = result['message']
    courses = SubElement(root, 'courses')

    for c in result['courses']:
        course = SubElement(courses, 'course')
        courseId = SubElement(course, 'course_id')
        courseId.text = c['course_id']
        name = SubElement(course, 'name')
        name.text = c['name']
        classroom = SubElement(course, 'classroom')
        classroom.text = c['classroom']
        classtime = SubElement(course, 'classtime')
        classtime.text = c['classtime']
        classtype = SubElement(course, 'type')
        classtype.text = c['type']
        department = SubElement(course, 'department')
        department.text = c['department']
        departmentId = SubElement(course, 'department_id')
        departmentId.text = c['department_id']

    return __xml + ET.tostring(root, encoding='utf-8', method='xml')

def loginResultToXml(result):
    root = Element('result')
    success = SubElement(root, 'success')
    success.text = result['success']
    message = SubElement(root, 'message')
    message.text = result['message']
    return __xml + ET.tostring(root, encoding='utf-8', method='xml')

def icourseStatisticsToXml(result):
    root = Element('listBean')
    for item in result:
        courseInfo = SubElement(root, 'courseInfo')
        courseId = SubElement(courseInfo, 'courseid')
        courseId.text = item['courseId']
        name = SubElement(courseInfo, 'name')
        name.text = item['name']
        institution = SubElement(courseInfo, 'institution')
        institution.text = item['institutionId']
        studentNum = SubElement(courseInfo, 'studentNum')
        studentNum.text = item['studentNum']

    return __xml + ET.tostring(root, encoding='utf-8', method='xml')

def istudentStatisticsToXml(result):
    root = Element('listBean')
    for item in result:
        studentInfo = SubElement(root, 'studentInfo')
        studentId = SubElement(studentInfo, 'studentid')
        studentId.text = item['studentId']
        name = SubElement(studentInfo, 'name')
        name.text = item['name']
        institution = SubElement(studentInfo, 'institution')
        institution.text = item['institutionId']
        courseNum = SubElement(studentInfo, 'courseNum')
        courseNum.text = item['courseNum']

    return __xml + ET.tostring(root, encoding='utf-8', method='xml')
